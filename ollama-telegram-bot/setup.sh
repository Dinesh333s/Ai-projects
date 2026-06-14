#!/bin/bash
# Quick setup script for Ollama Telegram Bot

echo "🤖 Ollama Telegram Bot - Quick Setup"
echo "===================================="
echo ""

# Check if script is being sourced
if [ "$BASH_SOURCE" == "$0" ]; then
    echo "❌ This script must be SOURCED, not executed!"
    echo "   Run: source ./setup.sh"
    exit 1
fi

# Prompt for token
echo "Enter your Telegram Bot Token (from BotFather):"
read -r TOKEN

if [ -z "$TOKEN" ]; then
    echo "❌ Token cannot be empty!"
    return 1
fi

# Set environment variable
export TELEGRAM_BOT_TOKEN="$TOKEN"

echo ""
echo "✅ Token set successfully!"
echo "   TELEGRAM_BOT_TOKEN=$TELEGRAM_BOT_TOKEN"
echo ""
echo "🚀 You can now run: python3 bot.py"
echo ""
echo "To make this permanent, add to ~/.zshrc:"
echo "   export TELEGRAM_BOT_TOKEN=\"$TOKEN\""

