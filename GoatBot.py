import random
import discord
from discord.ext import commands, tasks
import json
import math
import itertools
import requests
import asyncio
from bs4 import BeautifulSoup

hangman = False

ext = [".jpg",".png",".jfif",".jpeg",".gif",".mp4",".mp3",".svg",".tif",".mov",".PNG"]

requests_number = 0

quiz_songs = ["jw.mp3",""]

goat_pictures = ['https://res.cloudinary.com/sagacity/image/upload/c_crop,h_629,w_960,x_0,y_0/c_limit,f_auto,fl_lossy,q_80,w_1080/goats_brews_v65dzw.jpg','https://th.bing.com/th/id/OIP.AqtwG0qJER0oq_j9WKyZTwHaE8?pid=Api&rs=1','http://www.offthegridnews.com/wp-content/uploads/2015/01/goat-dealbreakerDOTcom.jpg','https://th.bing.com/th/id/OIP.7jVhWjUWPIDb3iWz3UhtQQHaF0?pid=Api&rs=1','http://mediad.publicbroadcasting.net/p/wwno/files/201409/20140902Goats02_web.jpg','https://th.bing.com/th/id/OIP.TlRzKyOHHyVSQvzjyxnoSgHaFj?pid=Api&rs=1','https://th.bing.com/th/id/OIP.4VDiVo923Jr5ZQSBMwsKDAHaEw?pid=Api&rs=1','http://diy.sndimg.com/content/dam/images/diy/fullset/2017/3/27/0/CI_Leanne-Lauricella-Prospect8.jpg.rend.hgtvcom.1280.1280.suffix/1490624026883.jpeg','https://i.ytimg.com/vi/wc81FriTWQo/maxresdefault.jpg','https://i.ytimg.com/vi/3NU33PXtf-4/maxresdefault.jpg']
client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    change_status.start()
    print('The goat is ready!')

@client.command()
async def goat(ctx):
    embed=discord.Embed(title="Goat Picture", description=f"Here is your goat picture! :)", color=0x4acdcf)
    embed.set_author(name="Goat", icon_url="https://th.bing.com/th/id/OIP.lEZkyumaONb59yvuaqzcuwAAAA?pid=Api&rs=1")
    embed.set_image(url=f"{random.choice(goat_pictures)}")
    await ctx.send(embed=embed)
    global requests_number
    requests_number = requests_number + 1

@client.command()
@commands.has_role("Nobility")
async def ban(ctx, user:discord.User, duration: int, method):
    multiplier = 1

    if method == "hour" or method == "hours":
        multiplier = 3600

        await ctx.guild.ban(user)

        embed=discord.Embed(title="Player Banned", description=f"{user} was banned by {ctx.author} for {duration} {method}. ", color=0xff0a0a)
        embed.set_author(name="Goat", icon_url="https://th.bing.com/th/id/OIP.lEZkyumaONb59yvuaqzcuwAAAA?pid=Api&rs=1")
        embed.set_thumbnail(url="http://www.clipartbest.com/cliparts/ncX/ByX/ncXByXMgi.gif")
        await ctx.send(embed=embed)

        await asyncio.sleep((duration*multiplier))
        await ctx.guild.unban(user)
        print("unbanned!")

    elif method == "minute" or method == "minutes":
        multiplier = 60

        await ctx.guild.ban(user)

        embed=discord.Embed(title="Player Banned", description=f"{user} was banned by {ctx.author} for {duration} {method}. ", color=0xff0a0a)
        embed.set_author(name="Goat", icon_url="https://th.bing.com/th/id/OIP.lEZkyumaONb59yvuaqzcuwAAAA?pid=Api&rs=1")
        embed.set_thumbnail(url="http://www.clipartbest.com/cliparts/ncX/ByX/ncXByXMgi.gif")
        await ctx.send(embed=embed)

        await asyncio.sleep((duration*multiplier))
        await ctx.guild.unban(user)
        print("unbanned!")
    elif method == "day" or method == "days":
        multiplier = 86400

        await ctx.guild.ban(user)

        embed=discord.Embed(title="Player Banned", description=f"{user} was banned by {ctx.author} for {duration} {method}. ", color=0xff0a0a)
        embed.set_author(name="Goat", icon_url="https://th.bing.com/th/id/OIP.lEZkyumaONb59yvuaqzcuwAAAA?pid=Api&rs=1")
        embed.set_thumbnail(url="http://www.clipartbest.com/cliparts/ncX/ByX/ncXByXMgi.gif")
        await ctx.send(embed=embed)

        await asyncio.sleep((duration*multiplier))
        await ctx.guild.unban(user)
        print("unbanned!")
    else:
        await ctx.send("Please use a valid method: hour(s), minute(s), or day(s).")



@client.command()
async def test(ctx):
    await ctx.send('testing 1234')
    global requests_number
    requests_number = requests_number + 1

@client.command()
@commands.has_role("Nobility")
async def shutdown(ctx):
    await ctx.bot.logout()

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    global requests_number
    requests_number = requests_number + 1

@commands.guild_only()
@client.command()
@commands.has_role('Nobility')
async def unlock(ctx):
    global requests_number
    requests_number = requests_number + 1
    await ctx.channel.set_permissions(ctx.guild.get_role(714868863061458985), send_messages=True)
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)

    embed=discord.Embed(title="Channel Unlocked", description=f"This channel was unlocked by {ctx.author}.", color=0x4acdcf)
    embed.set_author(name="Goat", icon_url="https://th.bing.com/th/id/OIP.lEZkyumaONb59yvuaqzcuwAAAA?pid=Api&rs=1")
    embed.set_thumbnail(url="https://www.freeiconspng.com/uploads/unlock-icon-18.png")
    await ctx.send(embed=embed)


@commands.guild_only()
@client.command()
@commands.has_role('Nobility')
async def lockdown(ctx):
    global requests_number
    requests_number = requests_number + 1
    await ctx.channel.set_permissions(ctx.guild.get_role(714868863061458985), send_messages=False)
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)

    embed=discord.Embed(title="Channel Lockdown", description=f"This channel was locked down by {ctx.author} ", color=0xe92b2b)
    embed.set_author(name="Goat", icon_url="https://th.bing.com/th/id/OIP.lEZkyumaONb59yvuaqzcuwAAAA?pid=Api&rs=1")
    embed.set_thumbnail(url="https://granicus.com/wp-content/uploads/image/png/lock-icon-red-circle.png")
    await ctx.send(embed=embed)

@client.command()
async def stats(ctx,player_name):
    page = requests.get(f"https://r6.tracker.network/profile/pc/{player_name}")
    soup = BeautifulSoup(page.content,'html.parser')
    KD = soup.select_one('div[data-stat="RankedKDRatio"]')
    WL = soup.select_one('div[data-stat="RankedWLRatio"]')
    HS = soup.select_one('div[data-stat="PVPAccuracy"]')
    RT = soup.select_one('div[data-stat="RankedTimePlayed"]')
    await ctx.send(f"Ranked KD: {KD.string}Ranked Win/Loss: {WL.string}Headshot Percentage: {HS.string}Ranked Time Played: {RT.string} ")


@client.command()
@commands.has_role('Nobility')
async def unmute(ctx,playername):
    global requests_number
    requests_number = requests_number + 1
    role = ctx.guild.get_role(757490893744767141)
    user = ctx.message.mentions[0]
    await user.remove_roles(role)

    embed=discord.Embed(title="Player Unuted", description=f"{playername} was unmuted by {ctx.author}.", color=0x277e26)
    embed.set_author(name="Goat", icon_url="https://th.bing.com/th/id/OIP.lEZkyumaONb59yvuaqzcuwAAAA?pid=Api&rs=1")
    embed.set_thumbnail(url="https://theslumbercurve.com/wp-content/uploads/2020/06/Checkmark-graphic.png")
    await ctx.send(embed=embed)

@client.command()
@commands.has_role('Nobility')
async def mute(ctx,playername):
    global requests_number
    requests_number = requests_number + 1
    role = ctx.guild.get_role(757490893744767141)
    user = ctx.message.mentions[0]
    await user.add_roles(role)

    embed=discord.Embed(title="Player Muted", description=f"{playername} was muted by {ctx.author}. ", color=0xff0a0a)
    embed.set_author(name="Goat", icon_url="https://th.bing.com/th/id/OIP.lEZkyumaONb59yvuaqzcuwAAAA?pid=Api&rs=1")
    embed.set_thumbnail(url="http://www.clipartbest.com/cliparts/ncX/ByX/ncXByXMgi.gif")
    await ctx.send(embed=embed)

@client.event
async def on_message(message):
    global hangman
    global ext
    if message.content.startswith('/hangman'):
        hangman = True
        dm_channel = await message.author.create_dm()
        await dm_channel.send("Please send your words for hangman:")
    elif hangman == True and message.channel.id == message.author.dm_channel.id:
        hangman = False
        dm_channel = await message.author.create_dm()
        await dm_channel.send(message.content)
    if message.attachments and not message.attachments[0].url.endswith(tuple(ext)):
        await message.delete()

    await client.process_commands(message)


@client.command()
async def hangman(ctx):
    print("Someone is playing hangman!")

@client.command()
async def leave(ctx):
    channel = ctx.author.voice.channel
    server = ctx.message.guild.voice_client
    await server.disconnect()
    global requests_number
    requests_number = requests_number + 1

@client.command()
async def musicquiz(ctx):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('C:/Users/owend/Music/jw.mp3'), after = lambda e: print('done', e))
    global requests_number
    requests_number = requests_number + 1

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name = f'{requests_number} requests.'))
