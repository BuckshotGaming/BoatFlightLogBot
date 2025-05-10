
import os
import discord
from discord.ext import commands
from flask import Flask
import threading

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

# Map folder placeholder - ensure it's created
MAP_FOLDER = "map"
os.makedirs(MAP_FOLDER, exist_ok=True)

# Start Flask server in a background thread
app = Flask(__name__)
@app.route("/")
def index():
    return "Boat Flight Log Bot is running."

def run_flask():
    app.run(host="0.0.0.0", port=10000)

threading.Thread(target=run_flask).start()

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")
    try:
        synced = await bot.sync_commands()
        print(f"✅ Synced {len(synced)} commands.")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")

@bot.slash_command(name="sendtestlog", description="Send a test flight log to the log channel.")
async def sendtestlog(ctx):
    await ctx.respond("🛫 This is a test message from the Boat Flight Log Bot.")

@bot.slash_command(name="setchannel", description="Set the current channel for flight logs.")
async def setchannel(ctx):
    os.environ["Log_Channel_ID"] = str(ctx.channel.id)
    await ctx.respond(f"✅ Log channel set to: {ctx.channel.name} ({ctx.channel.id})")

@bot.slash_command(name="status", description="Check if the bot is online and running.")
async def status(ctx):
    await ctx.respond("✅ Boat Flight Log Bot is online and operational.")

# Load token from environment variables
token = os.getenv("DISCORD_TOKEN") or os.getenv("DISCORD_BOT_TOKEN")
if not token:
    print("❌ DISCORD_TOKEN environment variable not found!")
else:
    print("✅ Token loaded. Starting bot...")

bot.run(token)
