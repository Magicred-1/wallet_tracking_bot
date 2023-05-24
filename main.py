import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

prefix = "!"
token = os.getenv("DISCORD_BOT_TOKEN")

bot = commands.Bot(
    command_prefix=prefix, intents=discord.Intents.all(), help_command=None
)

bot.remove_command("help")

@bot.event
async def on_ready():
    print("Wallet Tracker is ready")

cogfiles = [
    f"cogs.{filename[:-3]}" for filename in os.listdir("./cogs") if filename.endswith(".py")
]

for cog in cogfiles:
    try:
        bot.load_extension(cog)
    except Exception as e:
        print(f"Error loading {cog}: {e}")

bot.run(token)

for cog in cogfiles:
    try:
        bot.load_extension(cog)
    except Exception as e:
        print(f"Error loading {cog}: {e}")

bot.run(token)
