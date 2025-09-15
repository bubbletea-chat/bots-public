# 🌅 Morning Brief Bot

An intelligent morning briefing bot built for the BubbleTea Chat platform. Get personalized daily weather and news summaries delivered at your preferred wake-up time!

## 🌟 Features

- **Personalized Morning Briefs**: Customized weather and news based on your location and interests
- **Scheduled Delivery**: Automatic delivery at your preferred wake-up time
- **Interactive Onboarding**: Easy setup process with location, interests, and time preferences
- **Real-time Weather**: Current weather conditions and forecasts using OpenAI's web search
- **Curated News**: Relevant news headlines filtered by your selected topics
- **Persistent Storage**: User preferences stored in Supabase database
- **Rich UI Components**: Interactive pills and formatted messages
- **Flexible Commands**: Multiple ways to interact with the bot

## 🎯 How It Works

### Onboarding Flow
1. **Location Setup**: Enter your city and country (e.g., "London, UK")
2. **Interest Selection**: Choose from 9 news categories (Technology, Business, Sports, etc.)
3. **Wake Time**: Set your preferred morning brief delivery time (24-hour format)
4. **Completion**: Receive confirmation and quick action options

### Daily Briefings
- Automatically generated and delivered at your specified wake-up time
- Includes weather forecast with practical tips
- Contains 3-4 relevant news headlines with descriptions
- Formatted with emojis and easy-to-read structure

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- BubbleTea Chat SDK
- OpenAI API access
- Supabase database (optional, for persistent storage)

### Environment Variables
Create a `.env` file with the following variables:

```bash
# Required
OPENAI_API_KEY=your_openai_api_key_here
BUBBLETEA_API_KEY=your_bubbletea_api_key_here

# Supabase (for persistent storage)
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_service_role_key
```

### Setup

1. **Clone and Install**:
```bash
git clone https://github.com/bubbletea-chat/bubbletea
cd bots-public/morning-bot
pip install -r requirements.txt
```

2. **Configure Environment**:
```bash
cp .env.example .env
# Edit .env with your API keys
```

4. **Run the Bot**:
```bash
python bot.py
```

## 🎮 Available Commands

| Command | Description |
|---------|-------------|
| `start` or `hi` | Begin setup or restart onboarding |
| `help` | Show available commands |
| `update` | Change your preferences |
| `preview` | Generate a sample morning brief |
| `morning` or `brief` | Get today's morning brief |
| `generate` | Manually trigger a brief generation |
| `status` | View your current settings |


## 🔧 Architecture

### Core Components

**MorningBriefBot**: Main orchestrator handling user interactions and routing commands

**OnboardingManager**: Guides users through the setup process with state management

**UserPreferencesManager**: Manages user data persistence and state transitions

**WeatherService**: Fetches weather data using OpenAI's web search capabilities

**NewsService**: Retrieves relevant news headlines based on user interests

**MorningBriefScheduler**: Background service that generates and delivers daily briefs

**NotificationService**: Handles communication with the BubbleTea API

**StorageAdapter**: Provides abstraction for data persistence (Supabase implementation)


## 🤖 AI Integration

The bot leverages **OpenAI GPT-4** with web search capabilities to provide:

### Weather Summaries
- Real-time weather data for any location
- Current conditions and daily forecasts
- Practical weather tips and recommendations
- Concise, emoji-rich formatting

### News Headlines
- Latest breaking news and developments
- Local and regional relevance
- Category-specific filtering (Technology, Business, Sports, etc.)
- Brief, digestible descriptions

## 🧪 Testing

### Manual Testing
```bash
# Test the complete flow
python bot.py
```

### Test Commands
1. Send `start` - Test onboarding flow
2. Complete setup with valid location, interests, and time
3. Send `preview` - Test brief generation
4. Send `generate` - Test manual triggering
5. Send `status` - Verify preferences saved correctly

### Integration Testing
- Verify OpenAI API connectivity
- Test Supabase database operations
- Confirm BubbleTea API notifications
- Validate scheduler timing accuracy

## 🤝 Contributing

We welcome contributions to improve the Morning Brief Bot!

### 🚀 Quick Start for Contributors

1. **Fork and Setup**:
```bash
git fork https://github.com/your-org/morning-brief-bot
cd morning-brief-bot
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Environment Setup**:
```bash
cp .env.example .env
# Configure with your API keys
```

3. **Create Feature Branch**:
```bash
git checkout -b feature/your-enhancement
```

### 📝 Contribution Guidelines

#### What to Work On
- **New Features**: Additional news categories, weather alerts, reminder systems
- **UI/UX**: Better onboarding flow, more interactive components
- **Performance**: Caching, rate limiting, error resilience
- **Storage**: Alternative storage backends, data export/import
- **AI Enhancements**: Better summarization, sentiment analysis, trending topics

#### Code Standards
- Follow PEP 8 style guidelines
- Add docstrings to all functions and classes
- Use type hints for better code clarity
- Handle exceptions gracefully
- Write descriptive commit messages

#### Testing Your Changes
- Test the complete onboarding flow
- Verify all commands work correctly
- Check error handling for invalid inputs
- Ensure backward compatibility with existing users

### 🎯 Feature Ideas

**Beginner-Friendly**:
- Add more news categories (Local, Health, Science)
- Implement timezone support
- Create user settings export/import
- Add weather alerts for extreme conditions

**Intermediate**:
- Multi-language support for international users
- Voice message support for morning briefs
- Integration with calendar apps for event awareness
- Smart brief timing based on user activity

**Advanced**:
- Machine learning for personalized content ranking
- Real-time brief updates throughout the day
- Integration with smart home devices
- Analytics dashboard for usage patterns

### 📋 Pull Request Process

1. **Before Submitting**:
   - Ensure all tests pass
   - Update documentation for new features
   - Add configuration examples if needed
   - Test with different user scenarios

2. **PR Description**:
   - Clearly describe the problem solved
   - Include screenshots for UI changes
   - List any breaking changes
   - Mention related issues

3. **Review Process**:
   - Code review by maintainers
   - Automated testing validation
   - Documentation review
   - Manual testing in development environment

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI** for GPT-4 API and web search capabilities
- **Supabase** for reliable database hosting
- **BubbleTea Chat** platform for bot infrastructure
- **Contributors** who help improve the bot

## 📞 Support

Need help or found a bug?

1. **Check Documentation**: Review this README and code comments
2. **Search Issues**: Look for similar problems in GitHub Issues
3. **Create Issue**: Report bugs or request features
4. **Community**: Join our Discord for real-time help

## 🚀 Roadmap

### Version 2.0
- [ ] Multi-timezone support
- [ ] Voice message delivery
- [ ] Calendar integration
- [ ] Weather alert system

### Version 3.0
- [ ] Multi-language support
- [ ] Smart home integration
- [ ] Advanced personalization
- [ ] Analytics dashboard

---

**Stay informed, start your day right! ☀️**

*Built with ❤️ for the BubbleTea Chat community*
