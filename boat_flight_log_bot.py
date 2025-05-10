
    import discord
    from discord.ext import commands
    import os
    import json

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='/', intents=intents)

    # Load config
    with open("config.json", "r") as f:
        config = json.load(f)

    log_channel_id = int(config.get("Log_Channel_ID", 0))

    @bot.event
    async def on_ready():
        print(f"✅ Bot is online as {bot.user}")

    @bot.command()
    async def sendtestlog(ctx):
        test_message = (
            "🛫 **Test Flight Log**
"
            "**Route**: KSEA ➡ KSFO
"
            "**Flight Time**: 4h 15m
"
            "**Pilot**: Bucky"
        )
        await ctx.send(test_message)

    token = os.getenv("DISCORD_TOKEN") or os.getenv("DISCORD_BOT_TOKEN")
    bot.run(token)
