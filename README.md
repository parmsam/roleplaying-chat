# Roleplaying Chat Game

This is a roleplaying chat game where you play as Sadie, a 24-pound golden retriever exploring the world from a dog's perspective! The game is built with R Shiny and powered by AI, creating engaging adventures with dynamic storytelling and AI-generated images.

## Prerequisites

- OpenAI API key for GPT-4.1-nano
- Google Gemini API key for image generation

## Installation

1. Clone this repository:
```bash
git clone https://github.com/parmsam/roleplaying-chat.git
cd roleplaying-chat
```

2. Install required R packages. See `app.R` for the list of packages used.

3. Set up your environment variables:
   - Create a `.env` and `.Renviron` files in the project root
   - Add your API keys:
```
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

4. Run the application:
```r
shiny::runApp("app.R")
```

## 🎯 How to Play

1. **Start the Game**: Type `/start` followed by your quest choice number (e.g., `/start 1`)
2. **Make Choices**: The AI game master will present you with scenarios and options
3. **Enjoy the Adventure**: Watch as your choices shape Sadie's adventure
4. **See the Story Come to Life**: AI-generated images accompany each turn to visualize your journey

## 🛠️ Technical Features

- **AI-Powered Game Master**: Uses GPT-4.1-nano to create dynamic, responsive storytelling
- **Image Generation**: Integrates Google's Gemini API to generate contextual images for each scene
- **Interactive UI**: Clean, responsive interface built with Shiny and Bootstrap
- **Modular Design**: Separate prompt files and utility scripts for easy customization
- **Cross-Language Integration**: Combines R and Python for optimal functionality

## 🎨 Customization

### Modifying the Game

- **Change the Character**: Edit `welcome-message.md` to create a different protagonist
- **Add New Adventures**: Modify the quest options in `welcome-message.md`
- **Update Additional Info**: Change the `additional_info.md` file to provide different game context
- **Adjust AI Behavior**: Update `system-prompt.md` to change the game master's style
- **Customize Appearance**: Modify the CSS in `app.R` to change the visual theme

### Adding Features

The modular structure makes it easy to extend the game:
- Add new tools for the AI in `scripts/utilities.R`
- Implement additional image generation models
- Create new game modes or difficulty levels

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## ⚙️ Key Tools

- [Shiny](https://shiny.rstudio.com/) for the web framework
- [ellmer](https://ellmer.tidyverse.org/) for the AI integration
- [shinychat](https://posit-dev.github.io/shinychat/r/index.html) for the chat interface
- [Marimo](https://marimo.io/) for the Python playground notebook
