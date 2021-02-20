import discord
client = discord.Client
from discord.ext import commands
bot = commands.Bot(command_prefix='_')
import io
import aiohttp

@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')


@bot.event
async def on_message(message):
	if '/trout' in message.content:
		await message.channel.send('{}'.format(message.author.mention) + ' slaps ' + message.content[7:] + ' around a bit with a large trout')
		async with aiohttp.ClientSession() as session:
			async with session.get('https://upload.wikimedia.org/wikipedia/commons/1/16/Rainbow_trout_transparent.png') as resp:
				if resp.status != 200:
					return await message.channel.send('Could not download file...')
					data = io.BytesIO(await resp.read())
					await message.channel.send(file=discord.File(data, 'cool_image.png'))

bot.command()
async def trout(ctx):
	await ctx.channel.send('hi')

bot.run('DISCORD_TOKEN')
