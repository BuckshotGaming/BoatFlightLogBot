
from discord.ext import commands
import discord
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Slash command sync on startup
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.sync_commands()
        print(f"✅ Synced {len(synced)} commands.")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")

# Example command
@bot.slash_command(name="sendtestlog", description="Send a test flight log.")
async def sendtestlog(ctx):
    await ctx.respond("🛫 This is a test flight log message!", ephemeral=False)

# Load token from either possible env var
token = os.getenv("DISCORD_TOKEN") or os.getenv("DISCORD_BOT_TOKEN")
if not token:
    print("❌ DISCORD_TOKEN environment variable not found!")
else:
    print("✅ Token loaded. Starting bot...")

bot.run(token)
