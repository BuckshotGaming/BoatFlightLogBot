
import os
import json
from flask import Flask, send_from_directory
from threading import Thread
import discord
from discord.ext import commands
from discord.commands import Option, slash_command

# Load config
CONFIG_PATH = "config.json"
if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)
else:
    config = {}

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", config.get("discord_token", ""))
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID", config.get("log_channel_id", "0")))

# Flask app for live map
app = Flask(__name__)

@app.route('/map')
def serve_map():
    return send_from_directory('map', 'index.html')

@app.route('/map/<path:path>')
def serve_map_files(path):
    return send_from_directory('map', path)

def run_flask():
    app.run(host="0.0.0.0", port=5000)

# Discord bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot connected as {bot.user}")
    print("✅ Flask server running on /map")

@slash_command(name="setchannel", description="Set the current channel as the log output channel.")
async def setchannel(ctx):
    global LOG_CHANNEL_ID
    LOG_CHANNEL_ID = ctx.channel.id
    config['log_channel_id'] = str(LOG_CHANNEL_ID)
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f)
    await ctx.respond(f"✅ Log channel set to: {ctx.channel.mention}")

@slash_command(name="testlog", description="Send a simulated flight log.")
async def testlog(ctx):
    if LOG_CHANNEL_ID:
        channel = bot.get_channel(LOG_CHANNEL_ID)
        if channel:
            await channel.send("✈️ Test Flight Log:\nPilot: TestUser\nAircraft: Cessna 172\nFlight Time: 1h 10m")
            await ctx.respond("✅ Test log sent.")
        else:
            await ctx.respond("❌ Could not find log channel.")
    else:
        await ctx.respond("❌ Log channel not set. Use /setchannel first.")

def run_bot():
    bot.run(DISCORD_TOKEN)

# Start everything
if __name__ == "__main__":
    Thread(target=run_flask).start()
    run_bot()
