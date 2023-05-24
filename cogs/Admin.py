import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="load",
        description="Admin"
    )
    @commands.is_owner()
    async def load(self, ctx, extension):
        self.bot.load_extension(f"cogs.{extension}")
        await ctx.respond(f"Loaded {extension}", ephemeral=True)

    @commands.slash_command(
        name="unload",
        description="Admin"
    )
    @commands.is_owner()
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f"cogs.{extension}")
        await ctx.respond(f"Unloaded {extension}", ephemeral=True)

    @commands.slash_command(
        name="reload",
        description="Admin"
    )
    @commands.is_owner()
    async def reload(self, ctx):
        for cog in self.bot.cogs:
            self.bot.reload_extension(f"cogs.{cog}")
        await ctx.respond("Reloaded all cogs", ephemeral=True)

def setup(bot):
    bot.add_cog(Admin(bot))