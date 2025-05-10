
import discord
from discord.ext import commands
import os
from flask import Flask

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ Bot connected as {bot.user}")
    synced = await bot.sync_commands()
    print(f"🔁 Synced {len(synced)} slash commands.")

@bot.slash_command(name="sendtestlog", description="Send a test flight log.")
async def sendtestlog(ctx):
    await ctx.respond("🛩️ Test flight log posted successfully!")

@bot.slash_command(name="status", description="Check bot status.")
async def status(ctx):
    await ctx.respond("✅ Boat Flight Log Bot is online and running!")

# Flask app for live map
app = Flask(__name__)

@app.route('/')
def index():
    return "Boat Flight Log Bot is running."

@app.route('/map')
def map_view():
    return "<html><body><h1>Live Map Loading...</h1></body></html>"

if __name__ == "__main__":
    bot.loop.create_task(bot.start(os.getenv("DISCORD_TOKEN")))
    app.run(host="0.0.0.0", port=5000)
