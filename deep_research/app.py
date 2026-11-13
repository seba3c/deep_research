import os

import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager
from styles import CSS, JS, EXAMPLES, HEADER_HTML, LOGIN_HTML

load_dotenv(override=True)


def get_auth_credentials() -> tuple[str, str] | None:
    """Enable login only when a complete credential pair is configured."""
    username = os.getenv("GRADIO_USERNAME")
    password = os.getenv("GRADIO_PASSWORD")
    if not username and not password:
        return None
    if not username or not password:
        raise ValueError(
            "Set both GRADIO_USERNAME and GRADIO_PASSWORD to enable login, "
            "or leave both unset to disable login."
        )
    return username, password


async def run(query: str):
    async for status_update in ResearchManager().run(query):
        yield status_update


with gr.Blocks(title="Deep Research") as ui:
    gr.HTML(HEADER_HTML)

    with gr.Row(elem_classes="dr-query-row"):
        query_textbox = gr.Textbox(
            placeholder="Type a research question...",
            show_label=False,
            container=False,
            autofocus=True,
            elem_id="dr-query",
            scale=5,
        )
        run_button = gr.Button("Investigate", variant="primary", elem_id="dr-run", scale=1)

    gr.HTML('<div class="dr-examples-label">Try one</div>')
    gr.Examples(examples=EXAMPLES, inputs=query_textbox, elem_id="dr-examples")

    report = gr.Markdown(elem_id="dr-report")

    run_button.click(run, inputs=query_textbox, outputs=report)
    query_textbox.submit(run, inputs=query_textbox, outputs=report)


if __name__ == "__main__":
    ui.launch(
        auth=get_auth_credentials(),
        auth_message=LOGIN_HTML,
        # Gradio 6.32's SSR login path drops auth_message on Hugging Face Spaces.
        ssr_mode=False,
        css=CSS,
        js=JS,
        theme=gr.themes.Base(),
    )
