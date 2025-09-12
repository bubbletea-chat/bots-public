import bubbletea_chat as bt
from openai import OpenAI
from dotenv import load_dotenv

import json
import os
import requests

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
todos = []


def add_task(task: str):
    if task.lower() in todos:        
        return f"Task '{task}' already exists."
    else:
        todos.append(task.lower())
        return f"Task '{task}' added."


def remove_task(task: str):
    if task.lower() in todos:
        todos.remove(task.lower())
        return f"Task '{task}' deleted."
    return f"Task '{task}' not found."


def show_tasks():
    if not todos:
        return "Your todo list is empty."
    return todos


def clear_tasks():
    todos.clear()
    return "All tasks cleared."


def format_conversation(conversation):
    messages = []
    for entry in conversation:
        if entry["sender"] == "user":
            messages.append({"role": "user", "content": entry["content"]["text"]})
        elif entry["sender"] == "agent":
            messages.append({"role": "assistant", "content": entry["content"]["text"]})
    return messages


def get_conversations(conversation_uuid):
    url = f"https://backend.bubbletea.chat/v1/developer/conversations/{conversation_uuid}/messages"

    headers = {
        "X-API-Key": os.getenv("BUBBLE_TEA_API_KEY"),
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


@bt.config()
def get_config():
    return bt.BotConfig(
        name="agile-todo-bot",
        url=os.getenv("NGROK_URL"),
        is_streaming=False,
        
        display_name="To-Do Bot",
        subtitle="Organize your daily tasks",
        icon_emoji="📝",
        description="A simple bot to help you create, manage, and check off your to-do list.",
        
        subscription_monthly_price=0,
        
        visibility="public",
        
        initial_text="Hi! 👋 I can help you manage your to-do list. What task would you like to add first?"
    )


@bt.chatbot
def todo_bot(message: str, conversation_uuid: str):
    print("Received conversation_uuid:", conversation_uuid)
    history_messages = ''  
    conversation = get_conversations(conversation_uuid)
    if conversation:
        history_messages = format_conversation(conversation)

    messages = [
        {"role": "system", "content": "You are a task manager. Decide which function to call. Your output must always be a valid tool call (function call) or a clarifying question to the user if more info is required."},
        *history_messages,
        {"role": "user", "content": message}
    ]
    
    tools = [
        {
            "type": "function",
            "function": {
                "name": "add_task",
                "description": "Add a new todo item. If the user input is incomplete or refers to something relative to an existing task (e.g., 'also eggs' after 'buy milk'), infer the full task from context (e.g., 'buy eggs'). Avoid adding duplicates by checking for partial or semantic matches.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tasks": {
                            "type": "array",
                            "items": { "type": "string" },
                            "description": "List of tasks to add. Should be normalized to complete, standalone tasks even if the user input was partial."
                        }
                    },
                    "required": ["tasks"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "remove_task",
                "description": "Remove a todo item. Supports removal by exact task name or by number (e.g., 'remove 2', 'remove 2nd task').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "The exact task name to remove (e.g., 'buy milk')."
                        },
                        "index": {
                            "type": "integer",
                            "description": "The position number of the task in the list (1 = first task, 2 = second task, etc.)."
                        }
                    }
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "modify_task",
                "description": "Modify an existing todo item. You can specify either the task index, the exact task name, or a partial match of the task text. If the new text is a variation of an existing task (e.g., 'buy airpods' → 'buy 2 airpods'), it should update the existing task instead of adding a duplicate. If the task already contains a numeric quantity (e.g., 'buy 12 eggs') and the new input increases that quantity (e.g., 'add egg'), it should intelligently update the existing item ('buy 13 eggs') rather than creating a new one.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "The exact task name to update"
                        },
                        "index": {
                            "type": "integer",
                            "description": "The position number of the task in the list (1 = first task)"
                        },
                        "new_task": {
                            "type": "string",
                            "description": "The updated task text"
                        }
                    },
                    "required": ["new_task"]
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "show_tasks",
                "description": "Show all todo items",
                "parameters": {"type": "object", "properties": {}},
            },
        },
        {
            "type": "function",
            "function": {
                "name": "clear_tasks",
                "description": "Remove all tasks from the list.",
                "parameters": {"type": "object", "properties": {}}
            }
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )

    msg = response.choices[0].message

    print("Response from OpenAI:", msg)    

    if msg.tool_calls:
        tool_call = msg.tool_calls[0]
        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments or "{}")

        if name == "add_task":
            tasks = args["tasks"]
            result_list = []
            for task in tasks:
                result_list.append(add_task(task))
            result = "\n".join(result_list)

        elif name == "remove_task":
            if "index" in args and args["index"] is not None:
                idx = args["index"] - 1
                all_tasks = show_tasks()
                
                if 0 <= idx < len(all_tasks):
                    task_to_remove = all_tasks[idx]
                    result = remove_task(task_to_remove)
                else:
                    result = f"Invalid index {args['index']}"
            elif "task" in args and args["task"]:
                result = remove_task(args["task"])
            else:
                result = "You must provide either 'task' or 'index'"

        elif name == "modify_task":
            all_tasks = show_tasks()
            new_task = args.get("new_task")

            if "index" in args and args["index"] is not None:
                idx = args["index"] - 1
                if 0 <= idx < len(all_tasks):
                    old_task = all_tasks[idx]
                    all_tasks[idx] = new_task
                    result = f"Modified task {args['index']}: '{old_task}' → '{new_task}'"
                else:
                    result = f"Invalid index {args['index']}"

            elif "task" in args and args["task"]:
                if args["task"].lower() in all_tasks:
                    idx = all_tasks.index(args["task"].lower())
                    old_task = all_tasks[idx]
                    all_tasks[idx] = new_task.lower()
                    result = f"Modified: '{old_task}' → '{new_task}'"
                else:
                    result = f"Task not found: {args['task']}"

            else:
                result = "You must provide either 'task' or 'index' along with 'new_task'"

        elif name == "show_tasks":
            result = show_tasks()
            if isinstance(result, list):
                result = "Your tasks:\n" + "\n".join(f"{i}. {t}" for i, t in enumerate(result, start=1))

        elif name == "clear_tasks":
            result = clear_tasks()

        else:
            result = "Unknown tool"

        return bt.Text(result)

    return bt.Text(msg.content)


if __name__ == "__main__":
    bt.run_server(todo_bot, port=8000)
