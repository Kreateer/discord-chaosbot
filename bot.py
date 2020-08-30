import discord
from discord.ext import commands
from discord.utils import get
import praw
import random
import datetime as dt

# Assign variables to hold client and bot references
client = discord.Client()
bot = commands.Bot(command_prefix='.')

startupTime = dt.datetime.now()
bot.remove_command('help')


# This function reads the bot token from file
def read_token():
    with open('token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()


# Functions made to read the reddit app id and secret from file
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

# This is a list that holds all the cogs to be loaded.
cog_load = ['cogs.nsfw', 'cogs.roles']

# This loads the extensions (or cogs) listed above and creates a custom exception on error
if __name__ == '__main__':
    for cog in cog_load:
        try:
            bot.load_extension(cog)
        except Exception as e:
            print(f'Failed to load extenstion {cog_load}.', file=sys.stderr)
            traceback.print_exc()


# When called, this function writes the command and time when the command was used to file.
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


# This event sets the rich presence for the bot, signals ready status to console and writes to file.
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


# This makes sure that the bot doesn't reply to itself
async def on_message(self, message):
    if message.author.id == self.user.id:
        return


# Basic command that prints short info. about the bot and author.
@bot.command()
async def info(ctx):
    run_time = dt.datetime.now()
    await ctx.send("A bot made by 'Kreateer#9930' to bring a little Chaos to your server! :smirk:\n "
                   "GitHub: https://github.com/Kreateer/discord-chaosbot\n"
                   "*Written in Python 3.7 using 'discord.py'*")
    console_print("'info'", run_time)


# Basic command that tests if the bot has connected to Discord.
@bot.command()
async def ping(ctx):
    run_time = dt.datetime.now()
    await ctx.send('pong')
    console_print("'ping'", run_time)


# Basic help command that replaces the default, built-in one. It sends the list of commands to the user's DM.
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


bot.run(token, bot=True, reconnect=True)
