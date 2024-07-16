from configparser import ConfigParser
import discord
from discord.ext import commands
import os
import asyncio
from database.create import create_db

PREFIX = ["st"]
bot = commands.Bot(command_prefix=PREFIX, help_command=None, intents=discord.Intents.all())


# --------------------------------------
# bot event online
@bot.event
async def on_ready():
	for guild in bot.guilds:
		for member in guild.members:
			if not member.bot:
				print(member)

	print('\nБОТ ГОТОВ!!')
	for filename in os.listdir('./cogs'):
		for loading in os.listdir(f'./cogs/{filename}'):
			if loading.endswith('.py'):
				await bot.load_extension(f'cogs.{filename}.{loading[:-3]}')
				print(f"Загружен файл - |{filename}.{loading[:-3]}|")
	await bot.tree.sync()


@bot.event
async def on_member_join(member):
	if not member.bot:
		role = discord.utils.get(member.guild.roles, id=1259148927022796993)
		await member.add_roles(role)

# --------------------------------------


# bot start
async def main():
	await create_db()

	config = ConfigParser()
	config.read('config.ini')
	await bot.start(config['DEFAULT']['TOKEN'])


if __name__ == '__main__':
	asyncio.run(main())