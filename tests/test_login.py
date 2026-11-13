import os
from pathlib import Path
import runpy
import sys
import tempfile
from types import ModuleType
import unittest
from unittest.mock import Mock, patch

os.environ.setdefault("GRADIO_ANALYTICS_ENABLED", "False")

import gradio as gr
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.testclient import TestClient


APP_PATH = Path(__file__).resolve().parents[1] / "deep_research" / "app.py"
USERNAME = "test-user"
PASSWORD = "  dummy # password!$&  "


class LoginTests(unittest.TestCase):
    def load_app(self, environment=None, dotenv_path=None):
        research_module = ModuleType("research_manager")
        research_module.ResearchManager = Mock()
        self.addCleanup(research_module.ResearchManager.assert_not_called)
        environment = {
            "GRADIO_USERNAME": "",
            "GRADIO_PASSWORD": "",
            **(environment or {}),
        }
        # Never read the user's .env or import the real research agents.
        with (
            patch.dict(os.environ, environment),
            patch.dict(sys.modules, {"research_manager": research_module}),
            patch.object(sys, "path", [str(APP_PATH.parent), *sys.path]),
            patch("dotenv.load_dotenv") as dotenv_mock,
            patch.object(gr.Blocks, "launch", autospec=True) as launch,
        ):
            if dotenv_path is not None:
                dotenv_mock.side_effect = lambda **kwargs: load_dotenv(
                    dotenv_path, **kwargs
                )
            try:
                namespace = runpy.run_path(str(APP_PATH), run_name="__main__")
            except ValueError:
                launch.assert_not_called()
                raise
            dotenv_mock.assert_called_once_with(override=True)
            launch.assert_called_once()
            auth = launch.call_args.kwargs["auth"]
            self.assertEqual(launch.call_args.kwargs["auth_message"], namespace["LOGIN_HTML"])
            self.assertIs(launch.call_args.kwargs["ssr_mode"], False)
        return namespace, auth

    def test_credential_resolution(self):
        namespace, _ = self.load_app()
        resolve = namespace["get_auth_credentials"]
        cases = [
            ({}, None),
            ({"GRADIO_USERNAME": "", "GRADIO_PASSWORD": ""}, None),
            ({"GRADIO_USERNAME": ""}, None),
            ({"GRADIO_PASSWORD": ""}, None),
            (
                {"GRADIO_USERNAME": USERNAME, "GRADIO_PASSWORD": PASSWORD},
                (USERNAME, PASSWORD),
            ),
        ]
        for environment, expected in cases:
            with self.subTest(environment=environment), patch.dict(
                os.environ, environment, clear=True
            ):
                self.assertEqual(resolve(), expected)

    def test_partial_credentials_prevent_startup(self):
        for environment in (
            {"GRADIO_USERNAME": USERNAME},
            {"GRADIO_PASSWORD": PASSWORD},
        ):
            with self.subTest(environment=environment):
                with self.assertRaises(ValueError) as error:
                    self.load_app(environment)
                message = str(error.exception)
                self.assertIn("GRADIO_USERNAME", message)
                self.assertIn("GRADIO_PASSWORD", message)
                self.assertNotIn(USERNAME, message)
                self.assertNotIn(PASSWORD, message)

    def test_dotenv_credentials_override_environment(self):
        with tempfile.TemporaryDirectory() as directory:
            dotenv_path = Path(directory) / ".env"
            dotenv_path.write_text(
                f"GRADIO_USERNAME={USERNAME}\nGRADIO_PASSWORD='{PASSWORD}'\n"
            )
            _, auth = self.load_app(
                {"GRADIO_USERNAME": "old-user", "GRADIO_PASSWORD": "old-password"},
                dotenv_path=dotenv_path,
            )
        self.assertEqual(auth, (USERNAME, PASSWORD))

    def test_spaces_ssr_default_is_overridden(self):
        # Spaces enables SSR by default; retain the custom login HTML instead.
        self.load_app({
            "GRADIO_SSR_MODE": "True",
            "GRADIO_USERNAME": USERNAME,
            "GRADIO_PASSWORD": PASSWORD,
        })

    def make_client(self, environment=None):
        namespace, auth = self.load_app(environment)
        app = gr.mount_gradio_app(
            FastAPI(), namespace["ui"], path="/", auth=auth,
            auth_message=namespace["LOGIN_HTML"],
        )
        return TestClient(app)

    def test_login_protects_interface_and_research_endpoints(self):
        with self.make_client(
            {"GRADIO_USERNAME": USERNAME, "GRADIO_PASSWORD": PASSWORD}
        ) as client:
            login_page = client.get("/")
            self.assertEqual(login_page.status_code, 200)
            self.assertIn("dr-login-brand", login_page.text)
            self.assertIn("Sign in to continue", login_page.text)
            self.assertEqual(client.get("/config").status_code, 401)
            for endpoint in ("/gradio_api/queue/join", "/gradio_api/api/run"):
                self.assertEqual(
                    client.post(endpoint, json={"data": ["test query"]}).status_code,
                    401,
                )
            for username, password in (("wrong-user", PASSWORD), (USERNAME, "wrong")):
                response = client.post(
                    "/login", data={"username": username, "password": password}
                )
                self.assertEqual(response.status_code, 400)
                self.assertEqual(client.get("/config").status_code, 401)
            response = client.post(
                "/login", data={"username": USERNAME, "password": PASSWORD}
            )
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.json()["success"])
            self.assertEqual(client.get("/config").status_code, 200)

    def test_access_without_login_when_credentials_absent(self):
        with self.make_client() as client:
            page = client.get("/")
            self.assertEqual(page.status_code, 200)
            self.assertNotIn("dr-login-brand", page.text)
            self.assertEqual(client.get("/config").status_code, 200)


if __name__ == "__main__":
    unittest.main()
