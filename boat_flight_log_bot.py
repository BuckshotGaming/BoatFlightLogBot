
import discord
from discord.ext import commands
import json
import os

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.presences = True

bot = commands.Bot(command_prefix="/", intents=intents)

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

LOG_CHANNEL_ID = int(config.get("Log_Channel_ID", 0))
PILOT_ROLE_NAME = "Boat Pilot"
tracked_users = set()

@bot.event
async def on_ready():
    print(f"✅ Boat Flight Log Bot is now online as {bot.user}")
    print("🔄 Syncing all users with 'Boat Pilot' role...")
    for guild in bot.guilds:
        for member in guild.members:
            if any(role.name == PILOT_ROLE_NAME for role in member.roles):
                tracked_users.add(member.id)
    print(f"🛫 Tracking enabled for {len(tracked_users)} pilots.")

@bot.command()
async def sendtestlog(ctx):
    if ctx.channel.id != LOG_CHANNEL_ID:
        await ctx.send("❌ This command can only be used in the log channel.")
        return
    await ctx.send("🛫 Test flight log: N123AB from KSEA to KSFO. Duration: 2h 14m.")

**Aircraft**: TBM 930
**Departure**: CYVR
**Arrival**: CYYZ
**Flight Time**: 4h 15m")

@bot.command()
async def status(ctx):
    await ctx.send(f"✅ Boat Flight Log Bot is running.
Tracked Pilots: {len(tracked_users)}")

@bot.command()
async def recentflights(ctx):
    await ctx.send("📋 Recent flights feature is coming soon!")

@bot.command()
async def viewlog(ctx):
    await ctx.send("📖 The flight log system is active, but viewing full logs isn't ready yet.")

@bot.command()
async def trackme(ctx):
    tracked_users.add(ctx.author.id)
    await ctx.send(f"✅ Now tracking you, {ctx.author.display_name}. You will appear on the live map when flying.")

@bot.command()
async def togglelogs(ctx):
    if ctx.author.id in tracked_users:
        tracked_users.remove(ctx.author.id)
        await ctx.send(f"🛑 Flight logs disabled for {ctx.author.display_name}.")
    else:
        tracked_users.add(ctx.author.id)
        await ctx.send(f"🛫 Flight logs enabled for {ctx.author.display_name}.")

# Auto token detection
token = os.getenv("DISCORD_TOKEN") or os.getenv("DISCORD_BOT_TOKEN")
if not token:
    print("❌ DISCORD_TOKEN environment variable not found!")
else:
    print("✅ Token loaded. Starting bot...")

bot.run(token)
