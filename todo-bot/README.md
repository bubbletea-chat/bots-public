# AgileKode To-Do Bot

A simple chatbot-powered to-do list manager built with FastAPI, OpenAI, and BubbleTea Chat.

## Features

- Add, remove, modify, and clear to-do tasks via chat
- View your current to-do list
- Natural language interface powered by OpenAI GPT-4o-mini
- Web-based chat UI via BubbleTea Chat

## Requirements

- Python 3.8+
- [OpenAI API key](https://platform.openai.com/)
- [ngrok](https://ngrok.com/) (for public URL, optional)

## Installation

1. **Download and extract the ZIP file**  
   Download the project ZIP file and extract it. Then navigate to the extracted folder:
   ```sh
   unzip AI-todo-project.zip
   cd AI-todo-project
   ```

2. **Create and activate a virtual environment**  
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**  
   Create a `.env` file in the project root with the following content:
   ```env
   OPENAI_API_KEY=your-openai-api-key
   NGROK_URL=your-ngrok-url
   ```

5. **Start the local FastAPI server**  
   ```sh
   python main.py
   ```

6. **Expose your local server with ngrok**  
   In a new terminal, run:
   ```sh
   ngrok http 8000
   ```
   Copy the HTTPS forwarding URL provided by ngrok.

7. **Register your bot on BubbleTea**  
   Go to the [BubbleTea dashboard](https://bubbletea.chat/) and register your bot using the ngrok HTTPS URL as the webhook endpoint.
