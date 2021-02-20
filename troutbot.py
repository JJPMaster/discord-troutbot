import discord
client = discord.Client
from discord.ext import commands
bot = commands.Bot(command_prefix='_')
import io
import aiohttp
import os
TOKEN = os.environ['DISCORD_TOKEN']
image = 'https://upload.wikimedia.org/wikipedia/commons/1/16/Rainbow_trout_transparent.png'
@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')


@bot.event
async def on_message(message):
    if message.content.startswith('/trout'):
		if str(message.author) != 'TroutBot!#7528':
			await message.channel.send('{} slaps {} around a bit with a large trout'.format(message.author.mention, message.content[7:]) + the_image())
			async with aiohttp.ClientSession() as session:
				async with session.get(image) as resp:
					if resp.status != 200:
						return await message.channel.send('Could not download file...')
					data = io.BytesIO(await resp.read())
					await message.channel.send(file=discord.File(data, 'cool_image.png'))

		else:
			await message.channel.send('Please don\'t do that.')
@bot.command()
async def trout(ctx):
	await ctx.channel.send('hi')

bot.run(TOKEN)
