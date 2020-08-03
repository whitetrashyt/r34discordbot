# import the discord.py api
import discord
# just as on our github script we need to import rule34 api from LordOfPolls and urllib.request, aswell as xml parser
import urllib.request as u # requests xml files online
import xml.etree.ElementTree as et # parses our xml files
import rule34 # you already know
import random # for random PID
from discord.ext import commands as commands



# functions from our r34botdl script on the github
# the xml parse func
def xmlparse(str):
	xmlurl = u.urlopen(str)
	# opens the url/xml file 
	tree = et.parse(xmlurl)
	# sets our xml tree to the parsed xml file
	root = tree.getroot()
	for i in root.iter('post'):
		# for every root iteration in the sub-tree "post,"
		fileurl = i.attrib['file_url']
		return fileurl
def xmlfetchtags(str):
	xmlurl = u.urlopen(str)
	# opens the url/xml file 
	tree = et.parse(xmlurl)
	# sets our xml tree to the parsed xml file
	root = tree.getroot()
	for i in root.iter('post'):
		# for every root iteration in the sub-tree "post,"
		tags = i.attrib['tags']
		return tags
def xmlfetchcount(str):
	xmlurl = u.urlopen(str)
	# opens the url/xml file 
	tree = et.parse(xmlurl)
	# sets our xml tree to the parsed xml file
	root = tree.getroot()
	for i in root.iter('posts'):
		count = i.attrib['count']
		print('xml count is: ' + count)
		return count
client = commands.Bot(command_prefix='&') # you did had bot = commands but should actually be client ^-^ / oh my god thank you
Client = discord.Client() # define our client
# Set this for easy access
r = rule34.Rule34
# we define the xml grab and parse now as a func
def pidfix(str): # fixes our pid random generator with our max ammount
    print(str) # this is for debugging purposes, will remove later.
    ye = int(xmlfetchcount(r.urlGen(tags=str,limit=1))) # polls how many images there are for the specified tags
    stepo = ye / 42 # there are 42 posts on a page, so divide this by 42
    newpid = round(stepo) # rounds these so we dont have insane decimals
    return newpid
recurse = 0
def r34dl(str,int):
	print(f"int: {int}") # always use f-string :3
	
	if int > 2000:
		int = 2000
	print(f'int after rounding: {int}')
	int = random.randint(1,int)
	print(f'int after rand: {int}')
	xurl = r.urlGen(tags=str,limit=1,PID=int) # this causes a problem if the pages for a specific tab are not above or equal to the supplied integer. Too bad!
	
	wr = xmlparse(xurl)
	htags = xmlfetchtags(xurl)
	print(wr.lstrip('.'))
	if 'webm' in wr.lstrip('.'):
		if 'sound' not in str:
			print(f'fetched a webm, recursing.')
			wr = r34dl(str,pidfix(str))
		else:
			pass
	elif 'webm' not in wr:
		print('No webm found, not recursing.')
		print(xurl)
	return wr



def rprefix(str, r): 
	rstr = str.replace(r,"")
	return rstr



@client.event # an event to print on ready
async def on_ready():
	print(f'Logged in as {client.user.name}!') # always use f-string :3
	
@client.event # event that listens for message that contains our prefix and a command
async def on_message(message):
	if message.author == client.user:
		return
	# prints the message into our console for debug
	print(f"Message Content: {message.content}") # always use f-string :3

	if message.content.startswith('&porn'): # since discord.ext isn't working, we'll have to use a very unorthodox method
		tags = rprefix(message.content, '&porn')
		newint = pidfix(tags)
		print(newint)
		if newint > 2000:
			newint = 2000
		

		if newint > 1:
			answer = r34dl(tags,random.randint(1,newint))
		if newint < 1:
			answer = r34dl(tags,1)
		
		
		embed = discord.Embed(title=f'{message.content}', color=message.author.color)
		embed.set_author(name=f'{message.author.display_name}', icon_url=f'{message.author.avatar_url}')
		embed.set_thumbnail(url='https://rule34.paheal.net/themes/rule34v2/rule34_logo_top.png')
		embed.set_image(url=f'{answer}')
		embed.set_footer(text="Made by jess#3347, with help from Marloes#1337", icon_url='https://cdn.discordapp.com/avatars/268211297332625428/a_06db63e4477b4a327f8a689f559bf887.gif?size=128')

		if 'webm' in answer:
			await message.channel.send(answer)
		elif 'webm' not in answer:
			await message.channel.send(embed=embed)
				
	if message.content.startswith('&help'):
		embed = discord.Embed(title=f'Pornbot Help - Prefix is &', color=message.author.color)
		embed.set_author(name=f'{message.author.display_name}', icon_url=f'{message.author.avatar_url}')
		embed.set_image(url=f'https://pistuff.000webhostapp.com/commands.PNG')
		embed.set_footer(text='Made by jess#3347, with help from Marloes#1337',icon_url='https://cdn.discordapp.com/avatars/268211297332625428/a_06db63e4477b4a327f8a689f559bf887.gif?size=128')
		await message.channel.send(embed=embed)
	if message.content.startswith('&coin'):
		side = random.randint(1,2)
		try:
			if side == 1:
				await message.channel.send('The coin landed on heads')
			if side == 2:
				await message.channel.send('The coin landed on tails')
			else:
				pass
		except:
			print('you dont know how to program.')
			await message.channel.send('Jess obviously needs to learn how to program')
	if message.content.startswith('&d6'):
		args = rprefix(message.content,'&d6')
		if args == '':
			dside = str(random.randint(1,6))
			await message.channel.send(f'You rolled:' + ' ' + dside)
		else:
			try:
				aint = int(args)
			except:
				print(f'Looks like the idiots a user and tried to provide string instead of int.')
				await message.channel.send('Hey idiot, send an integer, not text. Example: 6')
			mx = 6 * aint
			total = str(random.randint(1,mx))
			
			await message.channel.send(f'You rolled a total of:' + ' ' + total)
	if message.content.startswith('&d8'):
		args = rprefix(message.content,'&d8')
		if args == '':
			dside = str(random.randint(1,8))
			await message.channel.send(f'You rolled:' + ' ' + dside)
		else:
			try:
				aint = int(args)
			except:
				print(f'Looks like the idiots a user and tried to provide string instead of int.')
				await message.channel.send('Hey idiot, send an integer, not text. Example: 6')
			mx = 8 * aint
			total = str(random.randint(1,mx))
			
			await message.channel.send(f'You rolled a total of:' + ' ' + total)
	if message.content.startswith('&d10'):
		args = rprefix(message.content,'&d10')
		if args == '':
			dside = str(random.randint(1,10))
			await message.channel.send(f'You rolled:' + ' ' + dside)
		else:
			try:
				aint = int(args)
			except:
				print(f'Looks like the idiots a user and tried to provide string instead of int.')
				await message.channel.send('Hey idiot, send an integer, not text. Example: 6')
			mx = 10 * aint
			total = str(random.randint(1,mx))
			
			await message.channel.send(f'You rolled a total of:' + ' ' + total)
	if message.content.startswith('&d12'):
		args = rprefix(message.content,'&d12')
		if args == '':
			dside = str(random.randint(1,12))
			await message.channel.send(f'You rolled:' + ' ' + dside)
		else:
			try:
				aint = int(args)
			except:
				print(f'Looks like the idiots a user and tried to provide string instead of int.')
				await message.channel.send('Hey idiot, send an integer, not text. Example: 6')
			mx = 12 * aint
			total = str(random.randint(1,mx))
			
			await message.channel.send(f'You rolled a total of:' + ' ' + total)
	if message.content.startswith('&dc'):
		c = rprefix(message.content,'&dc')
		print(c)
		d = c.split(' ')
		print(d)
		del d[0]
		# default values for variables
		b = '' # defined this first since its the only thing i need
		a = ''
		if d != [str]:
			try:
				a = str(d[0])
				b = str(d[1])
			except:
				if len(d) == 0:
					print('no arguments provided')
					await message.channel.send(f"Hey vegetable, you didn't provide an argument. If you did, contact jess and tell her to fix it.")
				if len(d) == 1:
					b = '' # reset it just incase, yknow?
					print('no second variable recieved, skipping.')
				else:
					await message.channel.send(f"That wasn't supposed to happen. Looks like jess programmed the bot incorrectly.")
					await message.channel.send(f"If this happens, send a screenshot to jess with what you did and what came up, and send her this:")
					await message.channel.send(f'ERRORCATCH: Else triggered when len(d) should be 0, 1, or 2.')
					
		print('a is equal to' + a)
		print('b is equal to' + b) # it is really this simple.

		if b == '':
			dside = str(random.randint(1,int(a)))
			await message.channel.send(f'You rolled:' + ' ' + dside)
		else:
			mx = int(a) * int(b)
			print('max is:' + str(mx))
			total = str(random.randint(1,mx))
			
			await message.channel.send(f'You rolled a total of:' + ' ' + total)




# logs in to the bot
client.run('enter token here')
