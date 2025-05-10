import os
import discord
from discord.ext import commands
from flask import Flask
import threading

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = os.getenv("DISCORD_TOKEN") or os.getenv("DISCORD_BOT_TOKEN")
LOG_CHANNEL_ID = None

@bot.event
async def on_ready():
    print(f"{bot.user} is now running!")

# /sendtestlog command
@bot.slash_command(name="sendtestlog", description="Send a test flight log to the log channel.")
async def sendtestlog(ctx):
    await ctx.respond("🛫 Test flight log:\n**Pilot**: TestPilot123\n**Aircraft**: Cessna 172\n**Departure**: CYVR\n**Arrival**: CYYC\n**Flight Time**: 4h 15m")

# /setchannel command
@bot.slash_command(name="setchannel", description="Set the current channel as the log output channel.")
async def setchannel(ctx):
    global LOG_CHANNEL_ID
    LOG_CHANNEL_ID = ctx.channel.id
    await ctx.respond(f"✅ This channel has been set as the log output.")

# /trackme placeholder
@bot.slash_command(name="trackme", description="Toggle live tracking on the map.")
async def trackme(ctx):
    await ctx.respond("🗺️ Tracking enabled. Your aircraft will appear on the live map once you start flying.")

# Optional web server for Render "keep alive"
app = Flask(__name__)

@app.route("/")
def index():
    return "Boat Flight Log Bot is live."

def run_flask():
    app.run(host="0.0.0.0", port=10000)

# Run web server in background thread
threading.Thread(target=run_flask).start()

# Run the bot
bot.run(TOKEN)

