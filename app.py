from flask import Flask
from pyrogram import Client, filters
import threading

app = Flask(__name__)

# ======================
# TELEGRAM DETAILS
# ======================

API_ID = 21295053
API_HASH = "297598578931dcc642c2519414079f8e"
BOT_TOKEN = "8852863411:AAHJeN2b7oHdWedNjG1wTb0uNYSSgs3JK4A"

# ======================
# BOT
# ======================

bot = Client(
    "mybot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ======================
# HOME PAGE
# ======================

@app.route("/")
def home():
    return "Bot Running Successfully"

# ======================
# START COMMAND
# ======================

@bot.on_message(filters.command("start"))
async def start(client, message):

    await message.reply_text(
        "🔥 Send Video Up To 2GB"
    )

# ======================
# VIDEO RECEIVE
# ======================

@bot.on_message(filters.video | filters.document)
async def video(client, message):

    await message.reply_text(
        "✅ Video Received Successfully"
    )

# ======================
# RUN BOT
# ======================

def run_bot():
    bot.run()

threading.Thread(target=run_bot).start()

# ======================
# RUN FLASK
# ======================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=10000
    )
