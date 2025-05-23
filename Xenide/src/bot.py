import discord
from discord.ext import commands
import os

# Load the bot token and command prefix from the config file
import json

with open('config.json') as config_file:
    config = json.load(config_file)

TOKEN = config['token']
PREFIX = config['prefix']

# Initialize the bot
bot = commands.Bot(command_prefix=PREFIX)

# Load commands from the commands directory
for filename in os.listdir('./src/commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')

# Event listener for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')

# Run the bot
bot.run(TOKEN)