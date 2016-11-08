import discord
from discord.ext import commands

class WowCog:
    """Custom Cog that had commands for WoW Memes"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flamewreathtest(self):
        """This does stuff!"""

        await self.bot.say("I will not move when Flame Wreath is cast!")

    @commands.command(pass_context=True, no_pm=True)
    async def flamewreath(self, ctx):
        """I will not move when Flame Wreath is cast!"""
        url = "https://www.youtube.com/watch?v=gcA6y7sxKcA"
        audio = self.bot.get_cog('Audio')
        if not audio:
            await self.bot.say("Audio module required. Load with: {}load audio".format(ctx.prefix))
            return
        await ctx.invoke(audio.play, url_or_search_terms=url)

def setup(bot):
    bot.add_cog(WowCog(bot))
