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

# Setup bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Flask app for live map
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

# Register slash commands using py-cord
@bot.slash_command(name="sendtestlog", description="Send a test flight log.")
async def sendtestlog(ctx):
    await ctx.respond("🛩️ Test flight log posted successfully!")

@bot.slash_command(name="status", description="Check if the bot is online.")
async def status(ctx):
    await ctx.respond("✅ Boat Flight Log Bot is online and operational.")

@bot.slash_command(name="flightstatus", description="Get the current flight status.")
async def flightstatus(ctx):
    await ctx.respond("📡 No active flight currently. (SimConnect integration pending)")

@bot.slash_command(name="trackme", description="Toggle visibility on the live flight map.")
async def trackme(ctx):
    await ctx.respond("📍 Toggled your visibility on the live map. (Sim data needed)")

@bot.slash_command(name="togglelogs", description="Enable or disable automatic log posting.")
async def togglelogs(ctx):
    await ctx.respond("🔁 Automatic flight logs toggled. (Feature not yet active)")

@bot.slash_command(name="viewlog", description="View the most recent flight log.")
async def viewlog(ctx):
    await ctx.respond("📋 Flight Summary:\n- Duration: 00:00\n- Distance: 0 NM\n- Aircraft: Unknown")

@bot.slash_command(name="recentflights", description="List your recent flights.")
async def recentflights(ctx):
    await ctx.respond("🕓 Recent Flights:\n1. Flight A\n2. Flight B\n3. Flight C (placeholder)")

@bot.event
async def on_ready():
    print(f"✅ Bot connected as {bot.user}")

def run_bot():
    bot.run(DISCORD_TOKEN)

# Run Flask + Bot
if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=5000)
