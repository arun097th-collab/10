from flask import Flask, render_template
from pyrogram import Client, filters
import threading

app = Flask(__name__)

# =========================
# TELEGRAM API DETAILS
# =========================

API_ID = 21295053
API_HASH = "297598578931dcc642c2519414079f8e"
BOT_TOKEN = "8852863411:AAHJeN2b7oHdWedNjG1wTb0uNYSSgs3JK4A"

# =========================
# BOT SETUP
# =========================

bot = Client(
    "video_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# =========================
# VIDEO STORE
# =========================

FILES = {}

# =========================
# START COMMAND
# =========================

@bot.on_message(filters.command("start"))
async def start(client, message):

    txt = """
🔥 Send Any Video Up To 2GB

Bot Will Generate:

✅ Stream Link
✅ MX Player Button
✅ VLC Button
✅ Download Button
"""

    await message.reply_text(txt)

# =========================
# RECEIVE VIDEO
# =========================

@bot.on_message(filters.video | filters.document)
async def receive_video(client, message):

    file_id = None
    file_name = "video.mp4"

    # VIDEO
    if message.video:
        file_id = message.video.file_id
        file_name = message.video.file_name or "video.mp4"

    # DOCUMENT
    elif message.document:
        file_id = message.document.file_id
        file_name = message.document.file_name or "video.mp4"

    unique_id = str(message.id)

    FILES[unique_id] = {
        "file_id": file_id,
        "file_name": file_name
    }

    # =========================
    # YOUR RENDER URL
    # =========================

    link = f"https://YOUR-APP-NAME.onrender.com/watch/{unique_id}"

    text = f"""
✅ Video Added Successfully

🎬 Watch Link:
{link}
"""

    await message.reply_text(text)

# =========================
# PLAYER PAGE
# =========================

@app.route("/watch/<video_id>")
def watch(video_id):

    if video_id not in FILES:
        return "Video Not Found"

    data = FILES[video_id]

    stream_url = f"https://YOUR-APP-NAME.onrender.com/file/{video_id}"

    html = f"""
<!DOCTYPE html>
<html>
<head>

<title>{data['file_name']}</title>

<meta name="viewport" content="width=device-width, initial-scale=1">

<style>

body{{
background:#0f172a;
font-family:Arial;
color:white;
padding:20px;
text-align:center;
}}

video{{
width:100%;
max-width:900px;
border-radius:15px;
margin-top:20px;
}}

.btn{{
display:block;
width:260px;
margin:15px auto;
padding:15px;
border-radius:12px;
text-decoration:none;
font-size:18px;
font-weight:bold;
}}

.mx{{
background:#00c853;
color:white;
}}

.vlc{{
background:#ff6d00;
color:white;
}}

.download{{
background:#2962ff;
color:white;
}}

</style>

</head>

<body>

<h2>{data['file_name']}</h2>

<video controls autoplay>
<source src="{stream_url}" type="video/mp4">
</video>

<a class="btn mx"
href="intent:{stream_url}#Intent;package=com.mxtech.videoplayer.ad;type=video/*;end">
Open In MX Player
</a>

<a class="btn vlc"
href="vlc://{stream_url}">
Open In VLC
</a>

<a class="btn download"
href="{stream_url}" download>
Download Video
</a>

</body>
</html>
"""

    return html

# =========================
# STREAM FILE
# =========================

@app.route("/file/<video_id>")
def stream(video_id):

    if video_id not in FILES:
        return "File Not Found"

    # IMPORTANT:
    # Here Real Telegram Streaming Logic Needed
    # This Demo Only Shows File ID

    file_id = FILES[video_id]["file_id"]

    return f"""
Telegram File ID:

{file_id}

(Here You Need Real Streaming Logic)
"""

# =========================
# RUN BOT
# =========================

def run_bot():
    bot.run()

threading.Thread(target=run_bot).start()

# =========================
# RUN FLASK
# =========================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=10000
    )
