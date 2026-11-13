---
title: deep_research
app_file: app.py
sdk: gradio
sdk_version: 6.32.0
python_version: "3.12"
---

# Deep Research

A research app built with the OpenAI Agents SDK, with a user interface implemented using Gradio. The Planner Agent plans web searches, the Search Agent summarizes results, the Writer Agent produces a report, and the Email Agent sends it by email or Pushover notification.

## Set up and run locally

Requires **Python >=3.12** and `uv`. Run these macOS/Linux commands from the `deep_research/` directory.

Create a virtual environment and install the app dependencies:

```bash
uv python install 3.12
uv venv --python 3.12
uv pip install --python .venv/bin/python -r requirements.txt
```

Create or update `.env` in this directory with your own credentials:

```dotenv
OPENAI_API_KEY=your-openai-api-key
DEFAULT_MODEL_NAME=gpt-5.4-mini
HOW_MANY_SEARCHES=5
USE_EMAIL=true
EMAIL_ADDRESS=you@example.com
EMAIL_SMTP_SERVER=smtp.example.com
EMAIL_APP_PASSWORD=your-email-app-password
```

Use an OpenAI API key with access to the configured model and web search. The model and search-count settings are optional and shown with their defaults. Email delivery sends the report to `EMAIL_ADDRESS` through SMTP port 587.

For Pushover delivery, replace the email settings with:

```dotenv
USE_EMAIL=false
PUSHOVER_USER=your-pushover-user-key
PUSHOVER_TOKEN=your-pushover-application-token
```

Every research run includes delivery; `USE_EMAIL=false` selects Pushover rather than turning notifications off. Keep `.env` local; do not commit or upload credentials. In the full source repository, use a single `.env` in either this directory or the repository root to avoid conflicting settings.

Start the app:

```bash
.venv/bin/python app.py
```

Open the URL printed by Gradio, usually [http://127.0.0.1:7860](http://127.0.0.1:7860). Enter a research question and click **Investigate**. Stop the server with `Ctrl+C`.
