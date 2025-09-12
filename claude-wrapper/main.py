import os

from anthropic import Anthropic
from dotenv import load_dotenv
import bubbletea_chat as bt

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
NGROK_URL = os.getenv("NGROK_URL")

client = Anthropic(api_key=ANTHROPIC_API_KEY)

memory = {}


@bt.config()
def get_config():
    return bt.BotConfig(
        name="claude-bot",
        url=NGROK_URL,
        is_streaming=False,
        display_name="Claude Bot",
        subtitle="Smart AI powered by Anthropic",
        icon_emoji="🤖",
        description="Ask me anything! Powered by Claude with memory support.",
        discoverable=True,
        initial_text="👋 Hi! I’m Claude, your AI assistant.",
        visibility="public")


@bt.chatbot
def claude_bot(message: str, conversation_uuid: str = None):
    print(f"Conversation {conversation_uuid}\nMessage: {message}")

    history = memory.get(conversation_uuid, [])
    history.append({
        "role": "user",
        "content": [{
            "type": "text",
            "text": message
        }]
    })
    history = history[-10:]
    memory[conversation_uuid] = history

    response = client.messages.create(model="claude-3-haiku-20240307",
                                      max_tokens=1000,
                                      messages=history)

    memory[conversation_uuid].append({
        "role": "assistant",
        "content": response.content
    })

    text_reply = "".join(block.text for block in response.content
                         if block.type == "text")
    return bt.Markdown(text_reply)


if __name__ == "__main__":
    bt.run_server(claude_bot, port=8000)
