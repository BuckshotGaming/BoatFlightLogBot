
import os
import threading
import discord
from discord.ext import commands
from flask import Flask, send_from_directory

# Load environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
LOG_CHANNEL_ID = os.getenv("LOG_CHANNEL_ID")

print(f"🔍 DISCORD_TOKEN from environment: {repr(DISCORD_TOKEN)}")
print(f"🔍 LOG_CHANNEL_ID from environment: {repr(LOG_CHANNEL_ID)}")

if not DISCORD_TOKEN:
    raise ValueError("❌ DISCORD_TOKEN not found or invalid!")
if not LOG_CHANNEL_ID:
    raise ValueError("❌ LOG_CHANNEL_ID not found or invalid!")

# Set up Discord bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Flask web app
app = Flask(__name__, static_folder="map")

@app.route('/')
def index():
    return "Boat Flight Log Bot is running!"

@app.route('/map')
def serve_map():
    return send_from_directory("map", "index.html")

@app.route('/map.js')
def serve_map_js():
    return send_from_directory("map", "map.js")

@app.route('/style.css')
def serve_map_css():
    return send_from_directory("map", "style.css")

@bot.event
async def on_ready():
    print(f"✅ Bot connected as {bot.user}")

def run_bot():
    bot.run(DISCORD_TOKEN)

if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=5000)
