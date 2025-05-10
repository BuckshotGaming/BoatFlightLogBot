
import os
import discord
from discord.ext import commands

# Load Discord token
token = os.getenv("DISCORD_TOKEN")
if not token:
    print("❌ DISCORD_TOKEN environment variable not found!")
else:
    print("✅ Token loaded. Starting bot...")

# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

# Bot setup
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Boat Flight Log Bot is online as {{bot.user}}")

# Example command
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Start bot
bot.run(token)
