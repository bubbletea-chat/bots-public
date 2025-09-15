# 🎬 Movie Guessing Game Bot

An interactive movie guessing game bot built for the BubbleTea Chat platform. Challenge your movie knowledge with AI-generated questions featuring hilariously bad movie plot descriptions!

## 🎮 Features

- **Interactive Quiz Flow**: Multi-stage game with era, difficulty, and genre selection
- **AI-Generated Questions**: Uses OpenAI GPT-4 to create unique movie quiz questions
- **Bad Plot Descriptions**: Deliberately vague and humorous movie summaries for extra challenge
- **Rich UI Components**: Interactive pills for seamless user experience
- **Score Tracking**: Keep track of your performance across multiple games
- **Session Management**: Maintains game state per user conversation

## 🚀 How It Works

1. **Start the Game**: Type 'start' to begin
2. **Choose Era**: Select from All, Classics, 2000s, 2010s, or Recent
3. **Pick Difficulty**: Choose All, Easy, Medium, or Hard
4. **Select Genre**: Pick from Action, Comedy, Drama, Sci-Fi, Horror, Romance, or All
5. **Play Quiz**: Answer 5 multiple-choice questions based on badly described movie plots
6. **View Results**: See your final score and play again!

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- BubbleTea Chat SDK
- OpenAI API access

### Setup

1. Clone this repository:
```bash
git clone <repository-url>
cd movie-game-bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your OpenAI API key
```

4. Run the bot:
```bash
python bot.py
```

## 🔧 Configuration

The bot uses the following configuration:
- **Name**: `movie-guessing-game`
- **Display Name**: `Movie Guessing Game`
- **Port**: `5000` (configurable)
- **Streaming**: Disabled for structured responses

## 📁 Project Structure

```
movie-game-bot/
├── bot.py          # Main bot implementation
├── README.md                  # This file
├── requirements.txt           # Python dependencies
└── .env.example              # Environment variables template
```

## 🤖 OpenAI Integration

The bot uses GPT-4 to generate movie quiz questions with:
- Badly written movie descriptions (humorous, vague, or misleading)
- Four multiple choice options per question
- Difficulty and genre-appropriate content
- JSON-structured responses for consistent parsing

## 🧪 Testing

To test the bot locally:

1. Ensure your OpenAI API key is configured
2. Run the bot: `python bot.py`
3. Test the complete flow:
   - Send "start" message
   - Select era, difficulty, and genre
   - Answer quiz questions
   - Verify scoring works correctly

## 🤝 Contributing

We welcome contributions! Here's how you can help improve the Movie Guessing Game Bot:

### 🚀 Quick Start for Contributors

1. **Fork the Repository**
   ```bash
   git clone https://github.com/your-username/movie-guessing-game-bot.git
   cd movie-guessing-game-bot
   ```

2. **Set Up Development Environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt

   # Set up environment variables
   cp .env.example .env
   # Edit .env with your OpenAI API key
   ```

3. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

### 📝 Types of Contributions

#### 🐛 Bug Reports
- Use the GitHub Issues template
- Include steps to reproduce
- Provide expected vs actual behavior
- Include your environment details

#### 💡 Feature Requests
- Check existing issues first
- Describe the problem you're solving
- Provide detailed implementation ideas
- Consider backward compatibility

#### 🔧 Code Contributions

**What to work on:**
- New game modes or difficulty levels
- Additional movie genres or eras
- UI/UX improvements
- Performance optimizations
- Better error handling
- Code documentation

**Code Standards:**
- Follow PEP 8 style guide
- Add docstrings to functions
- Keep functions focused and small
- Use meaningful variable names
- Add type hints where helpful

#### 🎨 UI/UX Improvements
- Enhanced pill interactions
- Better user feedback
- Improved error messages
- Accessibility features

### 🧪 Development Guidelines

#### Code Style
```python
# Good example
def generate_quiz(state: GameState) -> list:
    """Generate quiz questions using OpenAI API.

    Args:
        state: Current game state with user preferences

    Returns:
        List of UI components for the quiz
    """
    # Implementation here
```

#### Testing Your Changes
1. Test the complete game flow
2. Try edge cases (invalid inputs, API failures)
3. Verify pill interactions work correctly
4. Check session management across users

#### Pull Request Process
1. **Before Submitting:**
   - Test your changes thoroughly
   - Update documentation if needed
   - Follow the existing code style
   - Add comments for complex logic

2. **PR Description Should Include:**
   - What problem does this solve?
   - How did you test the changes?
   - Any breaking changes?
   - Screenshots/GIFs for UI changes

3. **After Submission:**
   - Respond to review feedback
   - Keep your branch up to date
   - Be patient with the review process

### 🎯 Contribution Ideas

**Easy/Beginner:**
- Add more movie eras (e.g., 1990s, 1980s)
- Improve error messages
- Add more emojis and visual feedback
- Fix typos in documentation

**Medium:**
- Add multiplayer support
- Implement hint system
- Add movie poster integration
- Create admin panel for question review

**Advanced:**
- Add machine learning for question difficulty
- Implement real-time leaderboards
- Add voice integration
- Create analytics dashboard

### 📋 Commit Message Guidelines

Use conventional commits:
```bash
feat: add 1990s era option
fix: handle OpenAI API timeout gracefully
docs: update installation instructions
style: format code with black
test: add unit tests for game state
refactor: simplify question generation logic
```

### 🔍 Code Review Process

1. All PRs require review from maintainers
2. Automated tests must pass
3. Code coverage should not decrease
4. Documentation must be updated for new features
5. Breaking changes require major version bump

### 💬 Getting Help

- **Discord**: Join our community chat
- **GitHub Discussions**: For general questions
- **Issues**: For bug reports and feature requests
- **Email**: maintainers@example.com

### 🏆 Recognition

Contributors will be:
- Added to the CONTRIBUTORS.md file
- Mentioned in release notes
- Invited to join the core team (for regular contributors)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for GPT-4 API
- BubbleTea Chat platform
- All our amazing contributors
- Movie enthusiasts who inspired this project

## 📞 Support

If you encounter any issues:
1. Check existing GitHub Issues
2. Search our documentation
3. Join our community Discord
4. Create a new issue with detailed information

---

**Made with ❤️ by the BubbleTea Chat community**

*Ready to test your movie knowledge? Start guessing! 🎬*
