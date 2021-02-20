import discord
client = discord.Client
from discord.ext import commands
bot = commands.Bot(command_prefix='_')
import io
import aiohttp
import os
TOKEN = os.environ['DISCORD_TOKEN']
image = 'px-Rainbow_trout_transparent.png'
self = 812453966025719808

@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')


@bot.event
async def on_message(message):
	if message.content.startswith('/trout'):
			await message.channel.send('{} slaps {} around a bit with a large trout'.format(message.author.mention, message.content[7:]), file=discord.File(image))

@bot.command()
async def trout(ctx):
	await ctx.channel.send('hi')

bot.run(TOKEN)
