# OpenAI Agents Deep Research

A research project built with the OpenAI Agents SDK, with a user interface implemented using Gradio. The Planner Agent turns a research question into web searches, the Search Agent gathers and summarizes results, the Writer Agent combines the findings into a detailed report, and the Email Agent delivers it by email or Pushover notification, depending on configuration.

> **Lab / experimentation project.** This repo is a learning lab, not a production system. 
> It is based on the [OpenAI Agents SDK week of the Master AI Agentic Engineering - build autonomous AI Agents](https://github.com/ed-donner/agents/tree/main/2_openai) by Ed Donner 
> 
> Author: Sebastian Castañeda.

## Set up locally

The app requires **Python >=3.12**. The commands below use Python 3.12 and `uv` on macOS or Linux. Run them from the repository root.

Install Python and the project dependencies:

```bash
uv python install 3.12
uv sync --python 3.12
```

Create a `.env` file in the repository root (or update your existing one) with your own credentials:

```dotenv
OPENAI_API_KEY=your-openai-api-key
DEFAULT_MODEL_NAME=gpt-5.4-mini
HOW_MANY_SEARCHES=5

# Email delivery (the default): sends the report to EMAIL_ADDRESS.
USE_EMAIL=true
EMAIL_ADDRESS=you@example.com
EMAIL_SMTP_SERVER=smtp.example.com
EMAIL_APP_PASSWORD=your-email-app-password
```

Use an OpenAI API key with access to the configured model and web search. `DEFAULT_MODEL_NAME` and `HOW_MANY_SEARCHES` are optional; the values above are their defaults.

To use Pushover instead of email, replace the delivery settings with:

```dotenv
USE_EMAIL=false
PUSHOVER_USER=your-pushover-user-key
PUSHOVER_TOKEN=your-pushover-application-token
```

Delivery is part of every research run: `USE_EMAIL=false` selects Pushover rather than disabling notifications. Keep `.env` local; do not commit or upload credentials.

## Run locally

```bash
uv run --python 3.12 deep_research/app.py
```

Open the local URL printed by Gradio, usually [http://127.0.0.1:7860](http://127.0.0.1:7860), and enter a research question. Stop the server with `Ctrl+C`.
