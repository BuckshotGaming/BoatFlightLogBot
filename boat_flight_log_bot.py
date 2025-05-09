
import os
from flask import Flask, send_from_directory
from discord.ext import commands
import discord

# ENV variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID", "0"))

# Flask setup
app = Flask(__name__)

@app.route('/map/<path:path>')
def serve_map_files(path):
    return send_from_directory('map', path)

@app.route('/map')
def serve_map_index():
    return send_from_directory('map', 'index.html')

@app.route('/')
def root():
    return 'Boat Flight Log Bot is running.'

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot connected as {bot.user}')

@bot.command(name='setchannel')
async def set_channel(ctx):
    global LOG_CHANNEL_ID
    LOG_CHANNEL_ID = ctx.channel.id
    await ctx.send(f'✅ Log channel set to {ctx.channel.name}.')

@bot.command(name='sendtestlog')
async def send_test_log(ctx):
    if LOG_CHANNEL_ID:
        channel = bot.get_channel(LOG_CHANNEL_ID)
        if channel:
            await channel.send('🛫 Test flight log: User Bucky departed KSEA heading for KLAX.')
        else:
            await ctx.send('❌ Log channel not found.')
    else:
        await ctx.send('❌ Log channel not set. Use !setchannel first.')

def run_bot():
    bot.run(DISCORD_TOKEN)

if __name__ == "__main__":
    import threading
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=5000)
