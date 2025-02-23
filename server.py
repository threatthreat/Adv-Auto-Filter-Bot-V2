import os
import threading
from flask import Flask
from pyrogram import Client

# Create Flask App
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Running", 200  # ✅ Koyeb Health Check Passes

def run_flask():
    port = int(os.getenv("PORT", 8080))  # ✅ Set Port Correctly
    app.run(host="0.0.0.0", port=port)

# Start Flask in a separate thread
flask_thread = threading.Thread(target=run_flask, daemon=True)
flask_thread.start()

# Start Telegram Bot
bot = Client("bot", api_id=int(os.getenv("APP_ID")), api_hash=os.getenv("API_HASH"), bot_token=os.getenv("BOT_TOKEN"))

bot.run()  # ✅ This keeps the bot running
