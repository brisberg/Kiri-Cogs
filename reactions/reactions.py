import discord
import os
from discord.ext import commands


class ReactionsCog:
    """Custom Cog that had commands for Reaction sounds"""

    def __init__(self, bot):
        self.cog_name = 'reactions'
        self.bot = bot

    async def _play(self, url, ctx):
        """Helper for aliasing Play in the Audio module"""
        audio = self.bot.get_cog('Audio')
        if not audio:
            await self.bot.say("Audio module required. Load with: {}load audio".format(ctx.prefix))
            return
        await ctx.invoke(audio.play, url_or_search_terms=url)

    async def _play_local(self, url, ctx):
        """Helper for aliasing Play_local in the Audio module"""
        audio = self.bot.get_cog('Audio')
        if not audio:
            await self.bot.say("Audio module required. Load with: {}load audio".format(ctx.prefix))
            return
        await ctx.invoke(audio.play_local, url_or_search_terms=url)

    @commands.command(pass_context=True, no_pm=True)
    async def fail(self, ctx):
        """You have failed horribly!"""
        await self._play("https://www.youtube.com/watch?v=1ytCEuuW2_A", ctx)

    @commands.command(pass_context=True, no_pm=True)
    async def goofy(self, ctx):
        """Goofy yell!"""
        await self._play("https://www.youtube.com/watch?v=MUL5w91dzbo", ctx)

    @commands.command(pass_context=True, no_pm=True)
    async def wilhelm(self, ctx):
        """Wilhelm Scream"""
        await self._play(os.path.join("data", self.cog_name,
                         "Wilhelm_Scream.ogg"), ctx)


def setup(bot):
    bot.add_cog(ReactionsCog(bot))
