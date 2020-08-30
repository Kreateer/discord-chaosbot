import discord
from discord.ext import commands


class NsfwCog(commands.Cog, name="NSFW Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def pussy(self, ctx):
        run_time = dt.datetime.now()
        lewd_images = reddit.subreddit('pussy').hot()
        random_post = random.randint(1, 10)
        submission = ...
        for i in range(0, random_post):
            submission = next(x for x in lewd_images if not x.stickied)

        await ctx.send(f"{submission.url}")
        embed.set_author(name=f"{submission.title}")
        embed.add_field(name=f'Posted by: {submission.author}', value=f"{submission.permalink}", inline=False)
        await ctx.send("Have some wet thot pussy ( ͡° ͜ʖ ͡°)" + ctx.message.author.mention)
        console_print("'pussy'", run_time)

    @commands.command()
    @commands.guild_only()
    async def moist(self, ctx):
        run_time = dt.datetime.now()
        lewd_soaked = reddit.subreddit('SoakedHentai+HentaiPussyPics').hot()
        random_post = random.randint(1, 100)
        embed = discord.Embed(color=discord.Color.red())
        submission = ...
        for i in range(0, random_post):
            submission = next(x for x in lewd_soaked if not x.stickied)

        await ctx.send(f"{submission.url}")
        embed.set_author(name=f"{submission.title}")
        embed.add_field(name=f'Posted by: {submission.author}', value=f"{submission.permalink}", inline=False)
        await ctx.send(embed=embed)
        # await ctx.send(f"{submission.title}")
        # await ctx.send("Have some moist anime girls ( ͡° ͜ʖ ͡°)" + ctx.message.author.mention)
        console_print("'moist'", run_time)

    # Basic help command that lists the NSFW commands to the user's DM if the user has the NSFW role.
    @commands.command(pass_context=True, name="help nsfw")
    @commands.guild_only()
    @commands.has_role("NSFW")
    async def helpnsfw(self, ctx):
        run_time = dt.datetime.now()
        msg_auth = ctx.message.author
        embed = discord.Embed(color=discord.Color.red())
        embed.set_author(name='NSFW Help')
        embed.add_field(name='.moist', value="Fetches NSFW images from the r/pussy subreddit", inline=False)
        await msg_auth.send(embed=embed)
        console_print("'help nsfw'", run_time)



def setup(bot):
    bot.add_cog(NsfwCog(bot))
