import os


import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext.commands import bot
from discord import File

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

client = discord.Client()

@bot.event
async def on_ready():
    print('Connected')

@client.event
async def on_ready():
        print(f'{client.user} has connected to Discord!')
        for guild in client.guilds:
            if guild.name == GUILD:
                break
        print(
             f'{client.user} is connected to the following guild:\n'
             f'{guild.name}(id: {guild.id})'
        )

@bot.command(pass_context=True)
async def test(ctx):
    await ctx.send('Working!', file=discord.File("cat.png"))

@client.event
async def on_message(message):
        if message.author == client.user:
            return

        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
                ),
        ]


        hitchhiker_quotes = [
                'There is an art, it says, or rather, a knack to flying. The knack lies in learning how to throw yourself at the ground and miss.',
                'It is a mistake to think you can solve any major problems just with potatoes.',
                'In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move.',
                'A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.',
        ]

        if message.content == 'towel!':
            #response = random.choice(brooklyn_99_quotes)
            response = random.choice(hitchhiker_quotes)
            await message.channel.send(response)

bot.run(TOKEN)
client.run(TOKEN)

