import discord
from discord.ext import commands
import json
from dotenv import load_dotenv
import os
from pretty_help import PrettyHelp, DefaultMenu

if os.path.isfile('.env'):
    load_dotenv('.env')
else:
    pass

token = os.environ['token']
# Get configuration.json
with open("configurations.json", "r") as config:
    data = json.load(config)
    prefix = data["prefix"]

bot = commands.Bot(prefix)
# Load cogs
initial_extensions = [
    "Cogs.Tools",
    "Cogs.Pokemon",
    "Cogs.Github"
]

print(initial_extensions)

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Failed to load extension {extension}")

menu = DefaultMenu(page_left="◀", page_right="▶", remove="❌")
bot.help_command = PrettyHelp(menu=menu, no_category="Commands")

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{bot.command_prefix}help"))
    print(discord.__version__)
bot.run(token)