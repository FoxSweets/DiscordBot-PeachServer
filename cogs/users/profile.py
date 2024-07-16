import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord import app_commands


class profile(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@app_commands.command(name="profile", description="Посмотреть свой профиль или профиль другого игрока!")
	async def _profile(self, interaction: discord.Interaction):
		emb = discord.Embed(title=f"Профиль", description=f'USER PROFILE', colour=discord.Color.brand_green())
		emb.set_author(name=interaction.user.name, icon_url=interaction.user.avatar)

		await interaction.response.send_message(embed=emb, ephemeral=True)


async def setup(bot):
	await bot.add_cog(profile(bot))