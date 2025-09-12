# 🧠 GPT Assistant Bot

A simple yet powerful OpenAI GPT-4 assistant bot built for the BubbleTea Chat platform. Experience threaded conversations with ChatGPT in a seamless chat interface!

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
```bash
cp .env.example .env
# Edit .env with your API keys
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
