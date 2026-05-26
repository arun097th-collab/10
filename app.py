from flask import Flask, render_template, request

# Start Command
@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "Send Video File Up To 2GB"
    )

# Video Receive
@bot.on_message(filters.video | filters.document)
async def video_receive(client, message):

    file_id = None
    file_name = "video.mp4"

    if message.video:
        file_id = message.video.file_id
        file_name = message.video.file_name or "video.mp4"

    elif message.document:
        file_id = message.document.file_id
        file_name = message.document.file_name or "video.mp4"

    unique_id = str(message.id)

    FILES[unique_id] = {
        "file_id": file_id,
        "file_name": file_name
    }

    link = f"https://YOUR-RENDER-URL.onrender.com/watch/{unique_id}"

    text = f"""
✅ Video Added

▶ Stream Link:
{link}
"""

    await message.reply_text(text)

# Watch Page
@app.route('/watch/<video_id>')
def watch(video_id):

    if video_id not in FILES:
        return "Video Not Found"

    data = FILES[video_id]

    stream_url = f"https://YOUR-RENDER-URL.onrender.com/stream/{video_id}"

    return render_template(
        'player.html',
        stream_url=stream_url,
        file_name=data['file_name']
    )

# Stream Route
@app.route('/stream/<video_id>')
def stream(video_id):

    if video_id not in FILES:
        return "Not Found"

    file_id = FILES[video_id]['file_id']

    return f"Telegram File ID: {file_id}"

# Run Bot Thread

def run_bot():
    bot.run()

threading.Thread(target=run_bot).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
