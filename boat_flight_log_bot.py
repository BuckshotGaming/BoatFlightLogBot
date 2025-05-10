
import discord
from discord.ext import commands
import os
import json

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

config_file = "config.json"

# Load config or create default
if not os.path.exists(config_file):
    with open(config_file, "w") as f:
        json.dump({"log_channel_id": None, "tracked_users": []}, f)

with open(config_file, "r") as f:
    config = json.load(f)


def save_config():
    with open(config_file, "w") as f:
        json.dump(config, f, indent=4)


@bot.event
async def on_ready():
    print(f"✅ Boat Flight Log Bot is online as {bot.user}")


@bot.command()
async def setchannel(ctx):
    config["log_channel_id"] = ctx.channel.id
    save_config()
    await ctx.send("✅ This channel has been set for flight logs.")


@bot.command()
async def sendtestlog(ctx):
    embed = discord.Embed(
        title="✈️ Flight Complete",
        color=discord.Color.blue()
    )
    embed.add_field(name="👨‍✈️ Pilot", value="TestPilot123", inline=True)
    embed.add_field(name="🛩️ Aircraft", value="Cessna 172", inline=True)
    embed.add_field(name="👥 Passengers", value="2", inline=True)
    embed.add_field(name="📦 Cargo", value="500 lbs", inline=True)
    embed.add_field(name="🛫 Departure", value="CYVR", inline=True)
    embed.add_field(name="🛬 Arrival", value="CYYC", inline=True)
    embed.add_field(name="⬆️ Cruise Altitude", value="11,000 ft", inline=True)
    embed.add_field(name="💨 Airspeed", value="110 kt", inline=True)
    embed.add_field(name="⏱️ Duration", value="4h 15m", inline=True)
    embed.set_footer(text="📘 Logged by Boat Flight Log Bot")
    await ctx.send(embed=embed)


@bot.command()
async def trackme(ctx):
    user_id = str(ctx.author.id)
    if user_id not in config["tracked_users"]:
        config["tracked_users"].append(user_id)
        await ctx.send("📡 You are now being tracked on the live flight map.")
    else:
        config["tracked_users"].remove(user_id)
        await ctx.send("🛑 You have been removed from live map tracking.")
    save_config()


@bot.command()
async def viewlog(ctx):
    await ctx.send("📘 Flight log view coming soon.")


@bot.command()
async def flightstatus(ctx):
    await ctx.send("🛫 Flight status check coming soon.")


@bot.command()
async def recentflights(ctx):
    await ctx.send("🕓 Recent flights feature coming soon.")


@bot.command()
async def status(ctx):
    await ctx.send("✅ Boat Flight Log Bot is online and ready.")


token = os.getenv("DISCORD_TOKEN") or os.getenv("DISCORD_BOT_TOKEN")
bot.run(token)
