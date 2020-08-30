import discord
from discord.ext import commands


class RolesCog(commands.Cog, name="Role Commands"):
    def __init__(self, bot):
        self.bot = bot

    # @commands.cooldown(1, 10, commands.BucketType.user)
    # @commands.guild_only()
    # @commands.command(pass_context=True)
    # async def addrole(self, ctx, role):
    #     run_time = dt.datetime.now()
    #     user_id = self.user
    #     member = client.get_user(int(user_id))
    #     add_role = discord.Member
    #     if role is None:
    #         await ctx.send("You have not specified a role! Please try again!")
    #     else:
    #         give_role = discord.utils.get(member.guild.roles, name=role)
    #         await member.add_roles(give_role)
    #         await ctx.send(f"The role {give_role} has been assigned to you!")
    #     # try:
    #     #     await discord.Member.add_roles(member, role)
    #     #     await ctx.send(f"{ctx.author.name} has been given the role {role.name}")
    #     # except:
    #     #     await ctx.send("Role not found! Make sure the role exists!")
    #     console_print("'addrole'", run_time)


    # Command that lets the user assign themselves a role
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(pass_context=True)
    @commands.guild_only()
    # @commands.has_role("Admin")
    async def addrole(self, ctx, user: discord.Member, role: discord.Role):
        run_time = dt.datetime.now()
        member = ctx.message.author
        # role = get(member.server.roles, name="Test")
        await user.add_roles(member, role)
        await ctx.send(f"{ctx.author.name} has been given the the role {role.name}")
        console_print("'addrole'", run_time)


def setup(bot):
    bot.add_cog(RolesCog(bot))