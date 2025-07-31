# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Please setup these settings before launching the bot.

# =============[General]=============
token = 'token' # this is your discord bot token. 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import discord
from discord.ext import commands as command
import urllib.request as u
import xml.etree.ElementTree as et
import rule34
import random
import time
import asyncio
import os
import requests
intents = discord.Intents(messages=True, guilds=True)
intents.message_content = True # probably an easier way to do this but i straight up   don't use discord.py anymore
ltime = time.asctime(time.localtime())
client = command.Bot(command_prefix='&', intents=intents)
Client = discord.Client(intents=intents) # edit 7/31/25 why do we initialize the discord client twice ? what crack was i on?
client.remove_command('help')
r = rule34.Rule34
def xmlparse(str):
	root = et.parse(u.urlopen(str))
	for i in root.iter('post'):
		fileurl = i.attrib['file_url']
		return fileurl
def xmlcount(str):
	root = et.parse(u.urlopen(str))
	for i in root.iter('posts'):
		count = i.attrib['count']
		return count
def pidfix(str):
	ye = int(xmlcount(r.urlGen(tags=str,limit=1)))
	ye = ye - 1
	return ye
def rdl(str,int):
	print(f'[INFO {ltime}]: integer provided: {int}')

	if int > 2000:
		int = 2000
	if int == 0:
		int == 0
		print(f'[INFO {ltime}]: Integer is 0, accommodating for offset overflow bug. ')	
	elif int != 0:	
		int = random.randint(1,int)
	print(f'[INFO {ltime}]: integer after randomizing: {int}')
	xurl = r.urlGen(tags=str,limit=1,PID=int)
	print(xurl)
	wr = xmlparse(xurl)
	
	if 'webm' in wr:
		if 'sound' not in str:
			if 'webm' not in str:
				print(f'[INFO {ltime}]: We got a .webm, user didnt specify sound. Recursing. user tags: {str}')
				wr = rdl(str,pidfix(str))
		else:
			pass
	elif 'webm' not in wr:
		print(f'[INFO {ltime}]: Not a webm, dont recurse.')
	return wr
async def statuschange(): # edit 7/31/25 - should probably redact this until we ensure this method still works and causes no issues
	while True:
		await client.change_presence(activity=discord.Game(name='with my pussy'))
		await asyncio.sleep(120) # changed to 120 to avoid ratelimit and ban
		await client.change_presence(activity=discord.Game(name='&help'))
		await asyncio.sleep(120)
# Definitions of bot events starts here
# ================================================================================================================
@client.event
async def on_ready():
	print(f'[INFO {ltime}]: Logged in as {client.user.name}!')
	await statuschange()
# Definitions of bot commands starts here
# ================================================================================================================
@client.command()
async def porn(ctx,*arg):
	answer = ''
	# this is inefficent but also the only way i can do this
	arg = str(arg)
	arg = arg.replace(',','')
	arg = arg.replace('(','')
	arg = arg.replace(')','')
	arg = arg.replace("'",'')
	print(f'[DEBUG {ltime}]: arg is now {arg}')
	waitone = await ctx.send("***:desktop: We're polling Rule34! Please wait a few seconds.***")
	newint = pidfix(arg)
	if newint > 2000:
		newint = 2000
		answer = rdl(arg,random.randint(1,newint))
	if newint > 1:

		answer = rdl(arg,random.randint(1,newint))
	elif newint < 1:
		if newint == 0:
			answer = rdl(arg,0)
		elif newint != 0:
			answer = rdl(arg,1)
   
	if 'webm' in answer:
		await waitone.delete
		await ctx.send(answer)
	elif 'webm' not in answer:
		embed = discord.Embed(title=f'Rule34: {arg}',color=ctx.author.color)
		embed.set_author(name=f'{ctx.author.display_name}',icon_url=f'{ctx.author.avatar.url}')
		embed.set_thumbnail(url='https://rule34.paheal.net/themes/rule34v2/rule34_logo_top.png')
		embed.set_image(url=f'{answer}')
		embed.set_footer(text="Pornbot 2.0 - Made By ihatedisc.ord",icon_url='https://cdn.discordapp.com/avatars/268211297332625428/e5e43e26d4749c96b48a9465ff564ed2.png?size=128')
		waitone.delete
		await ctx.send(embed = embed)
# ================================================================================================================
@client.command()
async def rr(ctx):
	bullet = random.randint(1,6)
	if bullet == 3:
		embed = discord.Embed(title=f'CRACK.')
		embed.set_author(name=f'{ctx.author.display_name} - Russian roulette',icon_url=f'{ctx.author.avatar.url}')
		embed.set_image(url=rdl('gore',random.randint(1,100)))
		embed.set_footer(text='Pornbot 2.0 - Made By ihatedisc.ord')
		await ctx.send(embed=embed)
	if bullet == 6:
		embed = discord.Embed(title=f'CRACK.')
		embed.set_author(name=f'{ctx.author.display_name} - Russian roulette',icon_url=f'{ctx.author.avatar.url}')
		embed.set_image(url=rdl('gore',random.randint(1,100)))
		embed.set_footer(text='Pornbot 2.0 - Made By ihatedisc.ord')
		await ctx.send(embed=embed)
	elif bullet != 3 or bullet != 6:
		await ctx.send('***Click...***')
# ================================================================================================================
@client.command()
async def rcoin(ctx):
	side = random.randint(1,100)
	if side == 50 or side > 50:
		embed = discord.Embed(title=f'NSFW Coinflip: Heads', color=ctx.author.color)
		embed.set_author(name=f'{ctx.author.display_name} - NSFW Coinflip',icon_url=f'{ctx.author.avatar.url}')
		embed.set_image(url=rdl('blowjob animated',random.randint(1,100)))
		embed.set_footer(text='Pornbot 2.0 - Made By ihatedisc.ord')
		await ctx.send(embed=embed)
	elif side < 50:
		embed = discord.Embed(title=f'NSFW Coinflip: Tails', color=ctx.author.color)
		embed.set_author(name=f'{ctx.author.display_name} - NSFW Coinflip',icon_url=f'{ctx.author.avatar.url}')
		embed.set_image(url=rdl('big_ass animated',random.randint(1,100)))
		embed.set_footer(text='Pornbot 2.0 - Made By ihatedisc.ord')
		await ctx.channel.send(embed=embed)
# ================================================================================================================
@client.command()
async def fcoin(ctx):
	side = random.randint(1,100)
	if side == 50 or side > 50:
		embed = discord.Embed(title=f'Furry Coinflip: Heads', color=ctx.author.color)
		embed.set_author(name=f'{ctx.author.display_name} - Furry Coinflip',icon_url=f'{ctx.author.avatar.url}')
		embed.set_image(url=rdl('furry blowjob animated',random.randint(1,100)))
		embed.set_footer(text='Pornbot 2.0 - Made By ihatedisc.ord')
		await ctx.channel.send(embed=embed)
	elif side < 50:
		embed = discord.Embed(title=f'Furry Coinflip: Tails', color=ctx.author.color)
		embed.set_author(name=f'{ctx.author.display_name} - Furry Coinflip',icon_url=f'{ctx.author.avatar.url}')
		embed.set_image(url=rdl('furry tail animated',random.randint(1,100)))
		embed.set_footer(text='Pornbot 2.0 - Made By ihatedisc.ord')
		await ctx.channel.send(embed=embed)
# ================================================================================================================
@client.command()
async def coin(ctx):
	side = random.randint(1,100)
	if side == 50 or side > 50:
		await ctx.channel.send('***The coin landed on heads***')
	if side < 50:
		await ctx.channel.send('***The coin landed on tails.***')
# ================================================================================================================
@client.command()
async def d6(ctx,arg=1):
	if arg == '':
		dside = str(random.randint(1,6))
		await ctx.channel.send(f'You rolled:' + ' ' + dside)
	else:
		try:
			aint = int(arg)
		except:
			print(f'Looks like the idiots a user and tried to provide string instead of int.')
			await ctx.channel.send('Hey idiot, send an integer, not text. Example: 6')
		mx = 6 * aint
		total = str(random.randint(1,mx))
			
		await ctx.channel.send(f'You rolled a total of:' + ' ' + total)
# ================================================================================================================
@client.command()
async def d8(ctx,arg=1):
	if arg == '':
		dside = str(random.randint(1,8))
		await ctx.channel.send(f'You rolled:' + ' ' + dside)
	else:
		try:
			aint = int(arg)
		except:
			print(f'Looks like the idiots a user and tried to provide string instead of int.')
			await ctx.channel.send('Hey idiot, send an integer, not text. Example: 6')
		mx = 8 * aint
		total = str(random.randint(1,mx))
			
		await ctx.channel.send(f'You rolled a total of:' + ' ' + total)
# ================================================================================================================
@client.command()
async def d10(ctx,arg=1):
	if arg == '':
		dside = str(random.randint(1,10))
		await ctx.channel.send(f'You rolled:' + ' ' + dside)
	else:
		try:
			aint = int(arg)
		except:
			print(f'Looks like the idiots a user and tried to provide string instead of int.')
			await ctx.channel.send('Hey idiot, send an integer, not text. Example: 6')
		mx = 10 * aint
		total = str(random.randint(1,mx))
		await ctx.send(f'You rolled a total of {total}')
# ================================================================================================================
@client.command()
async def d12(ctx,arg=1):
	if arg == '':
		dside = str(random.randint(1,12))
		await ctx.channel.send(f'You rolled:' + ' ' + dside)
	else:
		try:
			aint = int(arg)
		except:
			print(f'Looks like the idiots a user and tried to provide string instead of int.')
			await ctx.channel.send('Hey idiot, send an integer, not text. Example: 6')
		mx = 12 * aint
		total = str(random.randint(1,mx))
		await ctx.send(f'You rolled a total of {total}') 
# ================================================================================================================
@client.command()
async def dc(ctx,arg1,arg2 = 1):
	
	a = str(arg1)
	if str(arg2) != '':
		b = str(arg2)
	
	print('a is equal to' + a)
	print('b is equal to' + b) # it is really this simple.
	if b == '':
		dside = str(random.randint(1,int(a)))
		await ctx.channel.send(f'You rolled:' + ' ' + dside)
	else:
		mx = int(a) * int(b)
		print('max is:' + str(mx))
		total = str(random.randint(1,mx))
	await ctx.channel.send(f'You rolled a total of:' + ' ' + total)
# ================================================================================================================
@client.command()
async def help(ctx):
	embed=discord.Embed(title="Pornbot help", description="Prefix is &", color=0xff80ff)
	embed.set_author(name=f'{ctx.author.display_name}', icon_url=f'{ctx.author.avatar.url}')
	embed.add_field(name="'porn [tags]'", value="Polls rule34 for porn following your tags.", inline=False)
	embed.add_field(name="'d6 [dice]'", value="Rolls (a/multiple) 6 sided die. Change [dice] to add several.", inline=False)
	embed.add_field(name="'d8 [dice]'", value="Rolls (a/multiple) 8 sided die, change your [dice] argument to add several.", inline=False)
	embed.add_field(name="'d10 [dice]'", value="Rolls (a/multiple) 10 sided die, change your [dice] argument to add several.", inline=False)
	embed.add_field(name="'d12 [dice]'", value="Rolls (a/multiple) 12 sided die, change your [dice] argument to add several.", inline=False)
	embed.add_field(name="'dc <sides> [dice]'", value="Rolls a custom-sided die, change your <sides> argument to set sides, and your [dice] argument to add more dice.", inline=False)
	embed.add_field(name="'coin'", value="Flips a coin.", inline=False)
	embed.add_field(name="'rcoin'", value="Flips a coin and posts a nsfw image based on what you get.", inline=False)
	embed.add_field(name="'fcoin'", value="Flips a coin and posts a nsfw furry image based on what you get.", inline=False)
	embed.add_field(name="'rr'", value="Russian roulette. Posts gore images if gun goes off.", inline=False)
	embed.add_field(name="'shibe'", value="Posts an image of a Shiba inu.", inline=False)
	embed.add_field(name="'cat'", value="Posts an image of a cat.", inline=False)
	embed.add_field(name="'bird'", value="Posts an image of a bird.", inline=False)
	embed.add_field(name="'suggest'",value="Sends a link to the github to suggest features and improvements aswell as make bug reports.")
	embed.set_footer(text="Pornbot 2.0 - Made By ihatedisc.ord",icon_url='https://cdn.discordapp.com/avatars/268211297332625428/e5e43e26d4749c96b48a9465ff564ed2.png?size=128')
	await ctx.send(embed=embed)
# ================================================================================================================
@client.command()
async def suggest(ctx):
	await ctx.channel.send(f'***If you have a suggestion, make an issue on the github repo: https://github.com/whitetrashyt/r34discordbot/issues***')
# # ================================================================================================================
# @client.command()
# async def shibe(ctx):
# 	r = requests.get('https://shibe.online/api/shibes?count=1')
# 	y = r.json()
# 	embed= discord.Embed(title='Have a shibe.',color=0xff80ff)
# 	embed.set_author(name=f'{ctx.author.display_name}',icon_url=f'{ctx.author.avatar.url}')
# 	embed.set_image(url=f'{y[0]}')
# 	print(f"[INFO {ltime}]: IMG URL IS {y[0]}")
# 	embed.set_footer(text="Pornbot 2.0 - Made By ihatedisc.ord",icon_url='https://cdn.discordapp.com/avatars/268211297332625428/e5e43e26d4749c96b48a9465ff564ed2.png?size=128')
# 	await ctx.send(embed=embed)
# # ================================================================================================================
# @client.command()
# async def cat(ctx):
# 	r = requests.get('https://shibe.online/api/cats?count=1')
# 	y = r.json()
# 	embed = discord.Embed(title='Have a kitty.',color=0xff80ff)
# 	embed.set_author(name=f'{ctx.author.display_name}',icon_url=f'{ctx.author.avatar.url}')
# 	embed.set_image(url=f'{y[0]}')
# 	print(f"[INFO {ltime}]: IMG URL IS {y[0]}")
# 	embed.set_footer(text="Pornbot 2.0 - Made By ihatedisc.ord",icon_url='https://cdn.discordapp.com/avatars/268211297332625428/e5e43e26d4749c96b48a9465ff564ed2.png?size=128')
# 	await ctx.send(embed=embed)
# # ================================================================================================================
# @client.command()
# async def bird(ctx):
# 	r = requests.get('https://shibe.online/api/birds?count=1')
# 	y = r.json()
# 	embed= discord.Embed(title='Have a bird.',color=0xff80ff)
# 	embed.set_author(name=f'{ctx.author.display_name}',icon_url=f'{ctx.author.avatar.url}')
# 	embed.set_image(url=f'{y[0]}')
# 	print(f"[INFO {ltime}]: IMG URL IS {y[0]}")
# 	embed.set_footer(text="Pornbot 2.0 - Made By ihatedisc.ord",icon_url='https://cdn.discordapp.com/avatars/268211297332625428/e5e43e26d4749c96b48a9465ff564ed2.png?size=128')
# 	await ctx.send(embed=embed)
# # ================================================================================================================
# update 7/31/25 8am est : these commands are now defunct due to shibe.online no longer existing

client.run(token)
