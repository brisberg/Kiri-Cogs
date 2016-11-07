import discord
from discord.ext import commands

class WowCog:
    """Custom Cog that had commands for WoW Memes"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flamewreath(self):
        """This does stuff!"""

        await self.bot.say("I will not move when Flame Wreath is cast!")

def setup(bot):
    bot.add_cog(WowCog(bot))
