import discord
from discord.ext import commands


class TempCog:
    """Custom Cog that had commands for WoW Memes"""

    def __init__(self, bot):
        self.bot = bot

    async def _play(self, url, ctx):
        """Helper for aliasing Play in the Audio module"""
        audio = self.bot.get_cog('Audio')
        if not audio:
            await self.bot.say("Audio module required. Load with: {}load audio".format(ctx.prefix))
            return
        await ctx.invoke(audio.play, url_or_search_terms=url)

    @commands.command(pass_context=True, no_pm=True)
    async def temp(self, ctx):
        """I will not move when Flame Wreath is cast!"""
        await self._play("https://www.youtube.com/watch?v=gcA6y7sxKcA", ctx)


def setup(bot):
    bot.add_cog(TempCog(bot))
