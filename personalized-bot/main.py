import os

import bubbletea_chat as bt
import openai
from dotenv import load_dotenv

from questions import *


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NGROK_URL = os.getenv("NGROK_URL")

client = openai.OpenAI(api_key=OPENAI_API_KEY)

user_progress = {}


def start_quiz(user_id):
    user_progress[user_id] = {"step": 1, "answers": []}
    return question_1()


def get_result(user_id):
    """Evaluate answers using scoring rubric and return animal result"""
    answers = user_progress[user_id]["answers"]

    counts = {"A": 0, "B": 0, "C": 0, "D": 0}
    for ans in answers:
        if ans in counts:
            counts[ans] += 1

    top_choice = max(counts, key=counts.get)

    rubric = {
        "A": ("The Wolf 🐺", "Fierce, independent, adventurous. You thrive in freedom and follow your instincts."),
        "B": ("The Dolphin 🐬", "Social, communicative, and empathetic. You shine around others and love teamwork."),
        "C": ("The Cat 🐱", "Comfort-loving, reflective, and selective with your energy. You guard your peace and pounce only when needed."),
        "D": ("The Monkey 🐒", "Playful, curious, adaptable. You’re quick to learn, love exploring, and keep life fun.")
    }

    animal, description = rubric[top_choice]

    prompt = (
        f"The quiz result is {animal}. "
        f"Base description: {description}\n\n"
        "Rewrite this in 2–3 fun, playful sentences for the user."
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a fun personality quiz bot."},
            {"role": "user", "content": prompt}
        ]
    )

    fun_text = response.choices[0].message.content
    del user_progress[user_id]

    return [
        bt.Text("✨ Your Inner Animal is..."),
        bt.Markdown(f"**{animal}**"),
        bt.Text(fun_text)
    ]


@bt.config()
def get_config():
    return bt.BotConfig(
        name="agile-personalized-bot",
        url=NGROK_URL,
        is_streaming=False,

        display_name="Personalized Bot",
        subtitle="Discover your inner animal",
        icon_emoji="📝",
        description="A fun personality quiz bot to help you discover your inner animal through 5 playful questions.",
        
        subscription_monthly_price=0,
        discoverable=True,
        visibility="public",

        initial_text="Hi! 👋 I can help you discover your inner animal through 5 fun questions! At the end, our AI will reveal your inner animal 🦊🐉🦉. Type 'start' to begin!"
    )
    

@bt.chatbot
def personalized_bot(message: str, user_uuid: str = None,):
    """Process an answer and move user to next step"""

    if message.lower().strip() == "start":
        return start_quiz(user_uuid)

    if user_uuid in user_progress and "step" in user_progress[user_uuid]:
        step = user_progress[user_uuid]["step"]
        
        message_result = message.split(":")[0]

        if message_result.upper().strip() not in ["A", "B", "C", "D"]:
            return bt.Text("⚠️ Please answer with one of the options: A, B, C, or D.")
        
        user_progress[user_uuid]["answers"].append(message_result)
        user_progress[user_uuid]["step"] += 1

        if step == 1:
            return question_2()
        elif step == 2:
            return question_3()
        elif step == 3:
            return question_4()
        elif step == 4:
            return question_5()
        elif step == 5:
            return get_result(user_uuid)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a friendly personalized quiz chatbot that helps users with fun conversations."},
            {"role": "user", "content": message}
        ]
    )

    result = response.choices[0].message.content
    return [
        bt.Text(result),
        bt.Markdown("\n👉 To begin the Inner Animal Quiz, just type **start** 🐾")
    ]


if __name__ == "__main__":
    bt.run_server(personalized_bot, port=8000)
