import discord
from discord.ext import commands
import os
import json

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Track users who want to appear on the live map
tracked_users = set()

# Load config (such as channel ID)
with open("config.json", "r") as f:
    config = json.load(f)
log_channel_id = int(config.get("log_channel_id", 0))

@bot.event
async def on_ready():
    print(f"✅ Boat Flight Log Bot is now online as {bot.user}")
    print("Syncing commands...")

@bot.slash_command(name="sendtestlog", description="Send a test flight log to the log channel.")
async def send_test_log(ctx):
    await ctx.respond("🛫 Test flight log:\nPilot: TestPilot123\nAircraft: Cessna 172\nDeparture: CYVR\nArrival: CYYC\nFlight Time: 4h 15m")

@bot.slash_command(name="trackme", description="Toggle live tracking on the flight map.")
async def track_me(ctx):
    user_id = str(ctx.author.id)
    if user_id in tracked_users:
        tracked_users.remove(user_id)
        await ctx.respond("🛑 You have been removed from live tracking.")
    else:
        tracked_users.add(user_id)
        await ctx.respond("✅ You are now being tracked on the live flight map.")

# Run the bot
token = os.getenv("DISCORD_TOKEN") or os.getenv("DISCORD_BOT_TOKEN")
bot.run(token)
