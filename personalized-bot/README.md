# Personalized Bot

A fun personality quiz bot built with **FastAPI**, **OpenAI**, and **BubbleTea Chat** to help you discover your inner animal through 5 playful questions.

## ✨ Features

- 🐾 Engaging personality quiz with 5 fun questions  
- 🦁 Reveals your "inner animal" based on your answers  
- 🤖 Natural language interface powered by **OpenAI GPT-4o-mini**  
- 💬 Web-based chat UI via **BubbleTea Chat**  
- 🌍 Publicly discoverable and free to use  

## 📦 Requirements

- Python **3.8+**  
- [OpenAI API key](https://platform.openai.com/)  
- [ngrok](https://ngrok.com/) *(optional, for public URL exposure)*  

## ⚙️ Installation

1. **Clone the repository**
    ```sh
    git clone https://github.com/bubbletea-chat/bots-public
    cd personalized-bot
    ```

2. **Create and activate a virtual environment**
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set environment variables**  
    Create a `.env` file in the project root:
    ```
    OPENAI_API_KEY=your-openai-api-key
    NGROK_URL=your-ngrok-https-url
    ```

## 🚀 Usage

1. **Start the bot server**
    ```sh
    python main.py
    ```

2. **Expose your local server with ngrok (if needed)**  
    In a new terminal:
    ```sh
    ngrok http 8000
    ```
    Copy the HTTPS forwarding URL provided by ngrok.

3. **Register your bot on BubbleTea**
    - Go to the BubbleTea dashboard
    - Register your bot
    - Use the ngrok HTTPS URL as the webhook endpoint
