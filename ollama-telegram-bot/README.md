# Ollama Telegram Bot

A Telegram bot powered by Ollama for local AI interactions.

## Features

- ✅ Local AI model integration with Ollama
- ✅ Telegram bot interface with async support
- ✅ Real-time message processing
- ✅ YAML-based configuration
- ✅ Logging and error handling

## Installation

### 1. Install Dependencies

Using pip:
```bash
pip3 install -r requirements.txt
```

Or install individually:
```bash
pip3 install python-telegram-bot ollama pyyaml
```

### 2. Download Ollama Model

```bash
ollama pull ministral-3:3b-cloud
```

### 3. Configure the Bot

**Secure Method: Set as Environment Variable** (Recommended)

```bash
export TELEGRAM_BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
```

**Alternative: Edit config.yml**

```yaml
telegram:
  bot_token: "YOUR_TELEGRAM_BOT_TOKEN"
```

⚠️ **Important**: Never commit your token to git! See `SECRETS_MANAGEMENT.md` for details.

## Configuration (config.yml)

The bot uses `config.yml` for configuration:

```yaml
telegram:
  bot_token: "YOUR_TOKEN"

ollama:
  model: "ministral-3:3b-cloud"
  host: "http://localhost:11434"

bot:
  name: "Ollama Bot"
  description: "A Telegram bot powered by Ollama"

logging:
  level: "INFO"
  format: "%(asctime)s - %(levelname)s - %(message)s"
```

## Usage

### Start Ollama
```bash
ollama serve
```

### Run the Bot
```bash
python3 bot.py
```


## Commands

- `/start` - Get a welcome message with bot info
- Send any message for AI response

## Troubleshooting

See `OLLAMA_CONFIG.md` for detailed troubleshooting guide.

## License

MIT

