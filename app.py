from flask import Flask
from pyrogram import Client, filters
import threading
import asyncio

app = Flask(__name__)

# =========================
# TELEGRAM API
# =========================
API_ID = 21295053
API_HASH = "297598578931dcc642c2519414079f8e"
BOT_TOKEN = "8852863411:AAHJeN2b7oHdWedNjG1wTb0uNYSSgs3JK4A"
# =========================
# BOT
# =========================

bot = Client(
    "mybot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# =========================
# FLASK HOME
# =========================

@app.route("/")
def home():
    return "Bot Running Successfully"

# =========================
# START
# =========================

@bot.on_message(filters.command("start"))
async def start(client, message):

    await message.reply_text(
        "🔥 Bot Working"
    )

# =========================
# VIDEO
# =========================

@bot.on_message(filters.video | filters.document)
async def video(client, message):

    await message.reply_text(
        "✅ Video Received"
    )

# =========================
# BOT THREAD
# =========================

def start_bot():

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    bot.run()

# =========================
# START THREAD
# =========================

threading.Thread(target=start_bot).start()

# =========================
# MAIN
# =========================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=10000
    )
