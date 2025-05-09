import os
import discord
from discord.ext import commands
import random
import sys

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

# ✅ Secure and stable setup
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = 1370124659676287018  # your actual flight log channel

if not BOT_TOKEN:
    print("❌ BOT_TOKEN is missing or not set in environment variables.")
    sys.exit(1)

@bot.event
async def on_ready():
    print(f"{bot.user} is connected and ready.")
    try:
        synced = await bot.sync_commands()
        print(f"Synced {len(synced)} slash commands.")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

@bot.slash_command(name="sendtestlog", description="Send a simulated test flight log.")
async def send_test_log(ctx):
    await ctx.defer()

    log_fields = {
        "🛫 Departure": "Los Angeles Intl (KLAX)",
        "🛬 Arrival": "San Francisco Intl (KSFO)",
        "✈️ Aircraft": "Boeing 737 MAX",
        "🧍 Pilot": ctx.author.display_name,
        "📦 Cargo": f"{random.randint(5000, 20000)} lbs medical supplies",
        "🧑‍🤝‍🧑 Passengers": str(random.randint(80, 160)),
        "📏 Distance": f"{random.randint(300, 400)} NM",
        "⏱ Duration": f"{random.randint(45, 75)} min",
        "🚀 Cruise Altitude": f"{random.choice(['28,000 ft', '30,000 ft', '33,000 ft'])}",
        "💨 Airspeed": f"{random.randint(430, 480)} knots",
        "✅ Status": "Arrived safely",
    }

    embed = discord.Embed(
        title="🧾 Boat Flight Log (Test)",
        description="Here is a sample flight log from the Boat Flight Log Bot:",
        color=discord.Color.blue()
    )

    for key, value in log_fields.items():
        embed.add_field(name=key, value=value, inline=True)

    embed.set_footer(text="Boat Flight Log Bot • Buckshot Gaming")

    try:
        channel = await bot.fetch_channel(CHANNEL_ID)
        await channel.send(embed=embed)
        await ctx.followup.send("✅ Test log sent to the flight log channel.", ephemeral=True)
    except Exception as e:
        print(f"Failed to send embed: {e}")
        await ctx.followup.send("❌ Could not send log. Check bot permissions or channel ID.", ephemeral=True)

bot.run(BOT_TOKEN)


