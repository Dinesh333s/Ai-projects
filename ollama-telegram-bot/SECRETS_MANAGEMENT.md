# Secret Management Guide

## 🔐 Why Keep Tokens Secret?

Your Telegram bot token is sensitive. If exposed:
- ❌ Others can control your bot
- ❌ They can send messages pretending to be your bot
- ❌ They might access user data

## ✅ Recommended Methods

### Method 1: Environment Variables (BEST) ⭐

**Option A: In Terminal (Temporary)**

```bash
export TELEGRAM_BOT_TOKEN="your_token_here"
python3 bot.py
```

**Option B: In `.zshrc` or `.bash_profile` (Persistent)**

1. Open your shell config file:
```bash
nano ~/.zshrc
```

2. Add at the end:
```bash
export TELEGRAM_BOT_TOKEN="your_actual_token_here"
```

3. Save and reload:
```bash
source ~/.zshrc
```

4. Verify it's set:
```bash
echo $TELEGRAM_BOT_TOKEN
```

### Method 2: Use `.env` File with `.gitignore`

1. Create a `.env` file (already created):
```bash
TELEGRAM_BOT_TOKEN=your_token_here
```

2. It's already in `.gitignore` (won't be committed)

3. Update bot.py to read from `.env`:
```python
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
```

### Method 3: Config File (Less Secure)

1. Keep sensitive tokens in `config.yml`:
```yaml
telegram:
  bot_token: "your_token_here"
```

2. Add `config.yml` to `.gitignore` to prevent commits

3. Share a `config.example.yml` with placeholder values

## 🛡️ Security Best Practices

### ✅ DO:
- ✅ Use environment variables for production
- ✅ Add `.env` and config files to `.gitignore`
- ✅ Never commit tokens to git/GitHub
- ✅ Rotate tokens if accidentally exposed
- ✅ Use strong unique tokens per environment

### ❌ DON'T:
- ❌ Hardcode tokens in source files
- ❌ Share tokens via email or chat
- ❌ Commit `.env` or `config.yml` to git
- ❌ Use same token across dev/prod
- ❌ Log or print tokens

## 🚀 Setup Instructions

### Step 1: Set Your Token as Environment Variable

**On macOS/Linux:**

```bash
# Temporary (this session only)
export TELEGRAM_BOT_TOKEN="123456789:ABCdefGHIjklmnoPQRstuvWXYZabcdefgh"

# Permanent (add to ~/.zshrc)
echo 'export TELEGRAM_BOT_TOKEN="123456789:ABCdefGHIjklmnoPQRstuvWXYZabcdefgh"' >> ~/.zshrc
source ~/.zshrc
```

**In IntelliJ (IDE configuration):**

1. Go to **Run → Edit Configurations**
2. Select your Python configuration
3. Expand **Environment variables**
4. Add: `TELEGRAM_BOT_TOKEN=your_token_here`
5. Click OK

### Step 2: Verify It Works

```bash
# Check if token is set
echo $TELEGRAM_BOT_TOKEN

# Should output your token (if set correctly)
```

### Step 3: Update config.yml

Update to use placeholder (fallback only):

```yaml
telegram:
  bot_token: "YOUR_TELEGRAM_BOT_TOKEN"  # Will be overridden by env variable
```

### Step 4: Run the Bot

```bash
python3 bot.py
```

The bot will use the environment variable first, then fall back to config.yml.

## 🔍 How It Works

Your updated `bot.py` now:

1. Reads `TELEGRAM_BOT_TOKEN` from environment variable first
2. Falls back to `config.yml` if not set
3. Shows error if token is still the placeholder

```python
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") or config['telegram'].get('bot_token')
if TOKEN == "YOUR_TELEGRAM_BOT_TOKEN":
    print("⚠️  Error: TELEGRAM_BOT_TOKEN not set!")
    exit(1)
```

## 🆘 Troubleshooting

**Error: "TELEGRAM_BOT_TOKEN not set!"**
- Make sure environment variable is exported
- Try in a new terminal window
- Check with: `echo $TELEGRAM_BOT_TOKEN`

**Token works in terminal but not in IntelliJ**
- Set it in Run → Edit Configurations
- Check "Environment variables" field
- Format: `TELEGRAM_BOT_TOKEN=your_token`

**Forgot what your token is?**
- Go back to BotFather on Telegram
- Use `/start` then `/help`
- Or create a new bot to get a new token

## 📋 Files to Ignore

Already configured in `.gitignore`:
- `.env` - Environment variables file
- `config.yml` - Local configuration with secrets
- `.idea/` - IntelliJ settings
- `__pycache__/` - Python cache

## 🎯 Summary

| Method | Security | Ease | Recommended |
|--------|----------|------|-------------|
| Environment Variable | ✅ High | ⭐⭐ | ✅ YES (Best) |
| .env File | ✅ High | ⭐⭐⭐ | ✅ YES (Good) |
| config.yml | ⚠️ Medium | ⭐⭐⭐ | ⚠️ Fallback Only |
| Hardcoded | ❌ None | ⭐ | ❌ NEVER |

---

Use **environment variables** for maximum security! 🔐

