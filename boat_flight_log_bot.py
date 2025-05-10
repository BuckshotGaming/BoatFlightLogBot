import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Boat Flight Log Bot is online as {bot.user}")

@bot.slash_command(name="sendtestlog", description="Send a full test flight log.")
async def sendtestlog(ctx):
    embed = discord.Embed(
        title="✈️ Flight Complete",
        color=discord.Color.blue()
    )
    embed.add_field(name="👨‍✈️ Pilot", value="TestPilot123", inline=True)
    embed.add_field(name="🛩️ Aircraft", value="Cessna 172", inline=True)
    embed.add_field(name="👥 Passengers", value="2", inline=True)
    embed.add_field(name="📦 Cargo", value="150 lbs", inline=True)
    embed.add_field(name="🛫 Departure", value="CYVR", inline=True)
    embed.add_field(name="🛬 Arrival", value="CYYC", inline=True)
    embed.add_field(name="⬆️ Cruise Altitude", value="6,500 ft", inline=True)
    embed.add_field(name="💨 Airspeed", value="120 kt", inline=True)
    embed.add_field(name="⏱️ Duration", value="1h 45m", inline=True)
    embed.set_footer(text="📘 Logged by Boat Flight Log Bot")
    await ctx.respond(embed=embed)

# Bot token logic
token = os.getenv("DISCORD_TOKEN") or os.getenv("DISCORD_BOT_TOKEN")
if token:
    bot.run(token)
else:
    print("❌ DISCORD_TOKEN not set in environment variables.")
