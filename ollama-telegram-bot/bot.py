import os
import logging
import yaml
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import ollama

# Load configuration from YAML
def load_config(config_file="config.yml"):
    """Load configuration from YAML file"""
    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        return config
    except FileNotFoundError:
        print(f"Error: {config_file} not found!")
        return None

config = load_config()
if not config:
    exit(1)

# Configuration - Token from environment variable for security
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") or config['telegram'].get('bot_token')
if TOKEN == "YOUR_TELEGRAM_BOT_TOKEN":
    print("⚠️  Error: TELEGRAM_BOT_TOKEN not set!")
    print("Set it with: export TELEGRAM_BOT_TOKEN='your_token_here'")
    exit(1)

MODEL = config['ollama']['model']
OLLAMA_HOST = config['ollama']['host']

# Configure logging
logging.basicConfig(
    format=config['logging']['format'],
    level=getattr(logging, config['logging']['level'])
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message."""
    await update.message.reply_text(
        "🤖 Hi! I'm your Ollama-powered bot.\n\n"
        f"💬 I'm using the {MODEL} model.\n\n"
        "Send me a message, and I'll respond!"
    )

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle chat messages."""
    user_message = update.message.text

    try:
        # Generate response using Ollama
        response = ollama.chat(
            model=MODEL,
            messages=[{"role": "user", "content": user_message}]
        )

        bot_response = f"""
💬 Response from {MODEL}:
{response['message']['content']}
        """
        await update.message.reply_text(bot_response)

    except Exception as e:
        logger.error(f"Error generating response: {e}")
        await update.message.reply_text("Sorry, I encountered an error.")

def main():
    """Main function to run the bot."""
    if not TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN not set.")
        return

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    logger.info("Bot started successfully")
    application.run_polling()

if __name__ == "__main__":
    main()

