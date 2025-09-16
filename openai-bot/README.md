# 🧠 GPT Assistant Bot

A simple yet powerful OpenAI GPT-4 assistant bot built for the BubbleTea Chat platform. Experience threaded conversations with ChatGPT in a seamless chat interface!

## 🎬 Live Demo

**Try it now:** [https://bubbletea.chat/gpt-assistant/chat](https://bubbletea.chat/gpt-assistant/chat)

**Example Chat:** [View a sample conversation](https://bubbletea.chat/shared/wrhjUAYmHryp3XFZFauSYyCjypq4n8v3egC9RmvxtD8)

## 🌟 Features

- **GPT-4 Integration**: Powered by OpenAI's latest GPT-4 model for intelligent responses
- **Threaded Conversations**: Maintains conversation context across multiple exchanges
- **Async Processing**: Non-blocking message handling for optimal performance
- **Rich Markdown Support**: Formatted responses with markdown rendering
- **Session Management**: Per-user conversation threads for personalized experiences
- **Error Handling**: Robust error management with graceful fallbacks
- **Simple Setup**: Minimal configuration required to get started

## 🎯 How It Works

### Conversation Flow
1. **Message Input**: User sends a message through BubbleTea Chat
2. **Context Retrieval**: Bot retrieves conversation thread for context
3. **GPT Processing**: Message is processed by OpenAI GPT-4 with full context
4. **Response Generation**: AI-generated response is formatted and sent back
5. **Thread Update**: Conversation thread is updated with new exchange

### Key Components
- **LLM Integration**: Uses BubbleTea's LLM wrapper for OpenAI
- **Thread Management**: Maintains conversation continuity
- **Async API Calls**: Non-blocking HTTP requests to BubbleTea platform
- **Error Recovery**: Handles API failures gracefully

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- BubbleTea Chat SDK
- OpenAI API access

### Setup

1. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

2. **Environment Configuration**:
Create a new `.env` file by copying the `.env.example` template:
```bash
cp .env.example .env
```

Then edit the `.env` file and update the variables with your actual API keys:
```bash
# Open .env in your editor and replace the placeholder values
nano .env  # or use your preferred editor
```

3. **Required Environment Variables**:
```bash
OPENAI_API_KEY=your_openai_api_key_here
BUBBLETEA_API_KEY=your_bubbletea_api_key_here
```

### Running the Bot

```bash
python bot.py
```

## 🔧 Configuration Options

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `OPENAI_API_KEY` | OpenAI API key for GPT access | - | ✅ Yes |
| `BUBBLETEA_API_KEY` | BubbleTea platform API key | - | ✅ Yes |
| `BUBBLETEA_API_URL` | BubbleTea backend URL | `https://backend.bubbletea.chat` | ❌ No |
| `OPENAI_MODEL` | OpenAI model to use | `gpt-4` | ❌ No |
| `OPENAI_MAX_TOKENS` | Maximum response tokens | `1000` | ❌ No |
| `OPENAI_TEMPERATURE` | Response creativity (0-2) | `0.7` | ❌ No |

### Model Configuration
- **Default Model**: GPT-4 for best response quality
- **Token Limit**: 1000 tokens per response (configurable)
- **Temperature**: 0.7 for balanced creativity and accuracy
- **Context Window**: Full conversation history maintained

## 📱 Usage Examples

### Basic Conversation
```
User: "Hello! Can you help me with Python?"
Bot: "Hello! I'd be happy to help you with Python programming.
      What specific topic or problem would you like assistance with?"

User: "How do I read a file in Python?"
Bot: "Here are several ways to read a file in Python:

      **Method 1: Using with statement (recommended)**
      ```python
      with open('filename.txt', 'r') as file:
          content = file.read()
          print(content)
      ```

      This automatically handles file closing even if an error occurs..."
```

### Technical Discussion
```
User: "Explain async/await in Python"
Bot: "Async/await in Python is used for asynchronous programming, allowing you to write
      concurrent code that can handle multiple operations without blocking...

      **Key Concepts:**
      - `async def`: Defines a coroutine function
      - `await`: Pauses execution until the awaited operation completes
      - Event loop: Manages and executes async operations

      **Example:**
      ```python
      async def fetch_data():
          await some_async_operation()
          return data
      ```"
```

## 🏗️ Architecture

### Code Structure
```
bot.py
├── process_message_async()    # Async message processing
├── gpt_assistant()           # Main bot handler
└── API Integration           # BubbleTea platform communication
```

### Flow Diagram
```
User Message → BubbleTea Chat → Bot Handler → OpenAI GPT-4 → Response → BubbleTea API → User
```

## 📖 Code Walkthrough

### 1. **Main Bot Handler** (`gpt_assistant()`)
Located at `bot.py:47-69`, this is the entry point for all incoming messages:

```python
@bt.chatbot("chatgpt-assistant")
def gpt_assistant(message: str, user_uuid: str = None, thread_id: str = None, conversation_uuid: str = None):
```

**Key responsibilities:**
- Receives user messages from BubbleTea platform
- Manages thread creation for new conversations
- Launches async processing for non-blocking operation
- Returns immediate acknowledgment to user

### 2. **Thread Management** (`bot.py:52-55`)
Ensures conversation continuity:

```python
if not thread_id:
    thread_id = llm.create_thread(user_uuid)  # New conversation
```

- Creates new thread for first-time users
- Maintains existing thread for returning users
- Preserves conversation context across exchanges

### 3. **Async Message Processing** (`process_message_async()`)
Located at `bot.py:16-44`, handles the actual AI interaction:

```python
async def process_message_async(message: str, conversation_uuid: str, thread_id: str = None):
    llm = LLM(model="gpt-4", llm_provider="openai")
    response = llm.get_assistant_response(thread_id, message)
```

**Processing steps:**
1. Initialize GPT-4 model connection
2. Send message with thread context to OpenAI
3. Format response as Markdown component
4. Post response back to BubbleTea API

### 4. **Response Delivery** (`bot.py:28-44`)
Sends AI response back to user:

```python
url = f"https://backend.bubbletea.chat/v1/developer/conversation/{conversation_uuid}/message"
payload = {"sender": "agent", "content": content}

async with httpx.AsyncClient() as client:
    response_api = await client.post(url, json=payload, headers=headers)
```

- Uses httpx for async HTTP requests
- Authenticates with BubbleTea API key
- Handles errors gracefully without blocking

### 5. **Bot Configuration** (`bot.py:72-107`)
Defines bot metadata and behavior:

```python
@gpt_assistant.config
def get_config():
    return bt.BotConfig(
        name="chatgpt-wrapper",
        display_name="ChatGPT Thread Bot",
        is_streaming=False,
        # ... other configuration
    )
```

**Configuration elements:**
- Bot identification and display information
- Streaming behavior settings
- Welcome message for new users
- Public visibility for discovery

### 6. **Server Initialization** (`bot.py:110-111`)
Starts the bot server:

```python
if __name__ == "__main__":
    bt.run_server(gpt_assistant, port=5000, host="0.0.0.0")
```

- Binds to all network interfaces (0.0.0.0)
- Runs on port 5000 by default
- Handles incoming webhook requests from BubbleTea

### Key Design Patterns

1. **Async/Await Pattern**: Non-blocking message processing prevents timeout issues
2. **Thread-based Context**: Maintains conversation history for coherent interactions
3. **Component-based Responses**: Uses BubbleTea's component system for rich formatting
4. **Error Resilience**: Graceful error handling ensures bot availability
5. **Environment Configuration**: Secure API key management via environment variables

## 🧪 Development

### Local Testing
```bash
# Set up development environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export OPENAI_API_KEY="your_key_here"
export BUBBLETEA_API_KEY="your_key_here"

# Run bot
python bot.py
```

### Adding Features

**Example: Custom System Prompts**
```python
# Modify the LLM initialization
llm = LLM(
    model="gpt-4",
    llm_provider="openai",
    system_prompt="You are a helpful coding assistant specialized in Python."
)
```

**Example: Response Filtering**
```python
# Add content filtering before sending response
def filter_response(response: str) -> str:
    # Add your filtering logic here
    return response.replace("inappropriate_content", "[filtered]")
```

## 🔐 Security Considerations

- **API Key Protection**: Store API keys in environment variables, never in code
- **Input Validation**: Validate user inputs before processing
- **Rate Limiting**: Implement rate limiting to prevent API abuse
- **Error Sanitization**: Don't expose sensitive error details to users
- **Content Filtering**: Consider implementing content filters for inappropriate responses

## 🚀 Deployment

### Production Setup
```bash
# Set production environment variables
export ENVIRONMENT=production
export OPENAI_API_KEY="prod_key_here"
export BUBBLETEA_API_KEY="prod_key_here"

# Use process manager (PM2, systemd, etc.)
pm2 start gpt_assistant_bot.py --name "gpt-assistant"
```

### Docker Deployment
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "bot.py"]
```

## 📊 Monitoring

### Key Metrics
- Response time to user messages
- OpenAI API usage and costs
- Error rates and types
- User engagement and satisfaction

### Logging
```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add logging to track usage
logger.info(f"Processing message for user {user_uuid}")
logger.error(f"API error: {str(e)}")
```

## 🤝 Contributing

1. **Fork the Repository**
2. **Create Feature Branch**: `git checkout -b feature/amazing-feature`
3. **Make Changes**: Implement your improvements
4. **Add Tests**: Ensure functionality works correctly
5. **Commit Changes**: `git commit -m 'Add amazing feature'`
6. **Push to Branch**: `git push origin feature/amazing-feature`
7. **Open Pull Request**: Submit your contribution

### Contribution Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Include error handling
- Test with different conversation contexts
- Update README if adding new features

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

- **Documentation**: See BubbleTea Chat documentation
- **Issues**: Report bugs via GitHub issues
- **Community**: Join BubbleTea Chat community discussions
- **Email**: Contact support for enterprise needs

---

**Built with ❤️ for the BubbleTea Chat community**
