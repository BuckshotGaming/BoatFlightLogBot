
import os
import discord
from discord.ext import commands
from flask import Flask
import threading

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

app = Flask(__name__)

LOG_CHANNEL_ID = int(os.getenv("Log_Channel_ID", "0"))

@bot.event
async def on_ready():
    print(f"✅ Bot connected as {bot.user}")

@bot.slash_command(name="sendtestlog", description="Send a test log to the flight log channel.")
async def sendtestlog(ctx):
    if LOG_CHANNEL_ID:
        channel = bot.get_channel(LOG_CHANNEL_ID)
        if channel:
            await channel.send("🛫 This is a test message from Boat Flight Log Bot.")
            await ctx.respond("✅ Test log sent.", ephemeral=True)
        else:
            await ctx.respond("❌ Could not find the log channel.", ephemeral=True)
    else:
        await ctx.respond("❌ Log channel ID not set.", ephemeral=True)

@bot.slash_command(name="setchannel", description="Set this channel as the flight log output channel.")
async def setchannel(ctx):
    global LOG_CHANNEL_ID
    LOG_CHANNEL_ID = ctx.channel.id
    await ctx.respond(f"✅ Log channel set to: {ctx.channel.mention}", ephemeral=True)

@bot.slash_command(name="status", description="Check the bot status.")
async def status(ctx):
    await ctx.respond("✅ Boat Flight Log Bot is online and ready.", ephemeral=True)

@bot.slash_command(name="trackme", description="Toggle flight tracking visibility on the live map.")
async def trackme(ctx):
    await ctx.respond("🛰️ Toggled your live map tracking (this is just a stub).", ephemeral=True)

@bot.slash_command(name="flightstatus", description="Show your current flight status.")
async def flightstatus(ctx):
    await ctx.respond("✈️ Flight status feature coming soon!", ephemeral=True)

@bot.slash_command(name="viewlog", description="View your most recent flight log.")
async def viewlog(ctx):
    await ctx.respond("📋 Viewing recent flight log (stub).", ephemeral=True)

@bot.slash_command(name="recentflights", description="List recent flight logs.")
async def recentflights(ctx):
    await ctx.respond("🗂️ Listing recent flights (stub).", ephemeral=True)

@app.route('/')
def home():
    return "Boat Flight Log Bot is running."

def run_flask():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    token = os.getenv("DISCORD_TOKEN") or os.getenv("DISCORD_BOT_TOKEN")
    if not token:
        print("❌ DISCORD_TOKEN environment variable not found!")
    else:
        print("✅ Token loaded. Starting bot...")
        bot.run(token)
