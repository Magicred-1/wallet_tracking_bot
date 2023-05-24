import discord
from discord import Option
from discord.ext import commands
import requests
import re

COOLDOWN = 10 # seconds
REGEX_FOR_WALLET = r"^(0x)?[0-9a-fA-F]{40}$"

"""
    Defi Wallet Tracker - Wallet.py

"""
class WalletTrackerListView(discord.ui.View):
    """
        A View that lets you select pages for a paginator.
        With the list of wallets you can select the wallet you 
        are tracking and see the details of the wallet with embeds.
        (Debank API)
    """
    def __init__(self, ctx, entries):
        super().__init__()
        self.ctx = ctx
        self.entries = entries
        self.current = 0

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id == self.ctx.author.id:
            return True
        else:
            await interaction.response.send_message("You cannot use this", ephemeral=True)
            return False
        
    @discord.ui.button(label="Previous", style=discord.ButtonStyle.blurple)
    async def previous(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.current == 0:
            await interaction.response.send_message("You cannot go back", ephemeral=True)
        else:
            self.current -= 1
            await interaction.response.edit_message(embed=self.entries[self.current])

    @discord.ui.button(label="Next", style=discord.ButtonStyle.blurple)
    async def next(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.current == len(self.entries) - 1:
            await interaction.response.send_message("You cannot go forward", ephemeral=True)
        else:
            self.current += 1
            await interaction.response.edit_message(embed=self.entries[self.current])


class WalletCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="add_wallet", 
        description="Wallet"
    )
    @commands.cooldown(1, COOLDOWN, commands.BucketType.user)
    async def add_wallet(
        self, 
        ctx,
        wallet: Option(str, "Enter wallet address you want to track : ", required=True)
    ):
        if not re.match(REGEX_FOR_WALLET, wallet):
            await ctx.respond("Invalid wallet address", ephemeral=True)
        else:
            await ctx.respond(f"Wallet {wallet} has been added to your **tracked address list**.", ephemeral=True)

    @commands.slash_command(
        name="list_wallet",
        description="Wallet"
    )
    @commands.cooldown(1, COOLDOWN, commands.BucketType.user)
    async def list_wallet(
            self, 
            ctx
        ):
            await ctx.respond(
                "List of wallets", 
                view=WalletTrackerListView(
                    ctx,
                    [
                        discord.Embed(title="Wallet 1", description="Wallet 1 description"),
                        discord.Embed(title="Wallet 2", description="Wallet 2 description"),
                        discord.Embed(title="Wallet 3", description="Wallet 3 description"),
                        discord.Embed(title="Wallet 4", description="Wallet 4 description"),
                        discord.Embed(title="Wallet 5", description="Wallet 5 description"),
                    ]
                ),
                ephemeral=True
                )

    @commands.slash_command(
        name="remove_wallet",
        description="Wallet"
    )
    @commands.cooldown(1, COOLDOWN, commands.BucketType.user)
    async def remove_wallet(
            self, 
            ctx,
            wallet: Option(str, "Enter wallet address you want to remove from your tracking list : ", required=True)
        ):
            await ctx.respond(f"Wallet {wallet} removed", ephemeral=True)

    
def setup(bot):
    bot.add_cog(WalletCommands(bot))

