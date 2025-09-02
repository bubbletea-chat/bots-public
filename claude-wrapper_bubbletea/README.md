# Claude Wrapper Bubbletea

A simple CLI wrapper for Anthropic's Claude API, built using Bubbletea for an interactive UI.

## Features

- Interactive chat interface with Claude
- Easy configuration of API keys
- Supports multiple Claude models
- Clean and responsive Bubbletea UI

## Requirements

- Python 3.8+
- Anthropic API key
- ngrok (optional, for public URL exposure)

## Installation

```bash
git clone git@github.com:bubbletea-chat/bots-public.git
cd bots-public
cd claude-wrapper_bubbletea
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Set environment variables by creating a `.env` file in the project root:

```
ANTHROPIC_API_KEY=your-claude-api-key
NGROK_URL=your-ngrok-https-url
```

## Usage

Start the bot server:

```bash
python main.py
```

Expose your local server with ngrok (if needed). In a new terminal:

```bash
ngrok http 8000
```

Copy the HTTPS forwarding URL provided by ngrok.

## Register Your Bot on BubbleTea

1. Go to the BubbleTea dashboard.
2. Register your bot.
3. Use the ngrok HTTPS URL as the webhook endpoint.
