import discord
from discord.ext import commands
import praw
import random
import datetime as dt

client = discord.Client()
bot = commands.Bot(command_prefix='.')

startupTime = dt.datetime.now()
bot.remove_command('help')


def read_token():
    with open('token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()


def reddit_id():
    with open('reddit_tokens.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()


def reddit_secret():
    with open('reddit_tokens.txt', 'r') as f:
        lines = f.readlines()
        return lines[1].strip()


red_id = reddit_id()
red_scrt = reddit_secret()

reddit = praw.Reddit(client_id=red_id, client_secret=red_scrt,
                     user_agent='A fun chat bot for Discord made in Python v3.7 (by u/TrueGentlemanLudwig)')

with open('BotLogs.txt', 'a') as g:
    g.write('\n*CHAOS BOT IS READY TO WREAK HAVOC*\n')
    g.write(str(dt.datetime.now()))
    g.write('\n')


def console_print(commandname, commandtime):
    time = commandtime
    run_time = dt.datetime.now() - time
    print('')
    print('*CHAOS BOT*')
    print('Loading Time:', run_time)
    print('Current Time:', dt.datetime.now())
    print(f"{commandname} has been run!")
    print('*CHAOS BOT*')

    with open('BotLogs.txt', 'a') as f:
        f.write('\n*CHAOS BOT*\n')
        f.write('Loading Time: ')
        f.write(str(run_time))
        f.write('\nCurrent Time: ')
        f.write(str(dt.datetime.now()))
        f.write('\n')
        f.write(str(commandname))
        f.write(' has been run\n')
        f.write('*CHAOS BOT*\n')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Creating Chaos | .help'))  # Set rich presence on start
    print('*CHAOS BOT IS GETTING READY TO WREAK HAVOC*')
    loading_time = dt.datetime.now() - startupTime
    print('Loading time:', loading_time)
    print('Current Time:', dt.datetime.now())
    print('Loading Complete!')
    print('*CHAOS BOT IS READY TO CREATE CHAOS!*')

    with open('BotLogs.txt', 'a') as f:
        f.write('\n*CHAOS BOT IS READY TO WREAK HAVOC!*\n')
        f.write(str(dt.datetime.now()))
        f.write('\nTime to connect: ')
        f.write(str(loading_time))
        f.write('\n')


class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return '{0.author} slapped {1} because *{2}*'.format(ctx, to_slap, argument)


@bot.command()
async def slap(ctx, *, reason: Slapper):
    await ctx.send(reason)


@bot.command()
async def info(ctx):
    run_time = dt.datetime.now()
    await ctx.send("A bot made by 'Kreateer#9930' to bring a little Chaos to your server! :smirk: "
                   "\n*Written in Python 3.7 using 'discord.py'*")
    console_print("'info'", run_time)


@bot.command()
async def ping(ctx):
    run_time = dt.datetime.now()
    await ctx.send('pong')
    console_print("'ping'", run_time)


@bot.command()
async def moist(ctx):
    run_time = dt.datetime.now()
    lewd_images = reddit.subreddit('pussy').hot()
    random_post = random.randint(1, 10)
    submission = ...
    for i in range(0, random_post):
        submission = next(x for x in lewd_images if not x.stickied)

    await ctx.send(f"{submission.url}")
    await ctx.send("Have some moist pussy ( ͡° ͜ʖ ͡°)" + ctx.message.author.mention)
    console_print("'moist'", run_time)


@bot.command(pass_context=True)
async def help(ctx):
    run_time = dt.datetime.now()
    msg_auth = ctx.message.author
    embed = discord.Embed(
        color=discord.Color.red()
    )
    embed.set_author(name='Help')
    embed.add_field(name='.ping', value="Responds \'pong\'", inline=False)
    embed.add_field(name='.info', value='Provides some info. about the bot', inline=False)
    await msg_auth.send(embed=embed)
    console_print("'help'", run_time)


bot.run(token)
