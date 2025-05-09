import os
import threading
import discord
from discord.ext import commands
from discord import app_commands
from flask import Flask, send_from_directory

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
LOG_CHANNEL_ID = os.getenv("LOG_CHANNEL_ID")

print(f"🔍 DISCORD_TOKEN from environment: {repr(DISCORD_TOKEN)}")
print(f"🔍 LOG_CHANNEL_ID from environment: {repr(LOG_CHANNEL_ID)}")

if not DISCORD_TOKEN:
    raise ValueError("❌ DISCORD_TOKEN not found or invalid!")
if not LOG_CHANNEL_ID:
    raise ValueError("❌ LOG_CHANNEL_ID not found or invalid!")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

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
    try:
        synced = await bot.tree.sync()
        print(f"🔁 Synced {len(synced)} slash command(s).")
    except Exception as e:
        print(f"❌ Error syncing commands: {e}")

@bot.tree.command(name="setchannel", description="Set the log channel for flight logs.")
async def setchannel(interaction: discord.Interaction):
    await interaction.response.send_message("✅ Log channel set!")

@bot.tree.command(name="sendtestlog", description="Send a test flight log.")
async def sendtestlog(interaction: discord.Interaction):
    await interaction.response.send_message("🛩️ Test flight log posted successfully!")

@bot.tree.command(name="viewlog", description="View your last flight summary.")
async def viewlog(interaction: discord.Interaction):
    await interaction.response.send_message("📋 Flight Summary:
• Origin: KSEA
• Destination: KSFO
• Duration: 1h 23m")

@bot.tree.command(name="recentflights", description="View your 5 latest flights.")
async def recentflights(interaction: discord.Interaction):
    await interaction.response.send_message("🕓 Recent Flights:
1. KSEA → KSFO
2. KSFO → KLAX
3. KLAX → KPDX
4. KPDX → KDEN
5. KDEN → KSEA")

@bot.tree.command(name="trackme", description="Toggle your visibility on the live map.")
async def trackme(interaction: discord.Interaction):
    await interaction.response.send_message("🛰️ Map tracking toggled!")

@bot.tree.command(name="flightstatus", description="Get current aircraft info.")
async def flightstatus(interaction: discord.Interaction):
    await interaction.response.send_message("🛫 Aircraft: C172
📡 Speed: 122kts
📍 Altitude: 3500ft")

@bot.tree.command(name="togglelogs", description="Enable or disable your flight logging.")
async def togglelogs(interaction: discord.Interaction):
    await interaction.response.send_message("🔧 Logging preference updated.")

@bot.tree.command(name="status", description="Show bot status.")
async def status(interaction: discord.Interaction):
    await interaction.response.send_message("✅ Bot is online and fully operational.")

def run_bot():
    bot.run(DISCORD_TOKEN)

if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=5000)
