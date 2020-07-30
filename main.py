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

# asynch calls needs us to sync r34 each time
r = rule34.Sync()
# we define the xml grab and parse now as a func
def r34dl(tags,int):
    print(int)
    xurl = r.URLGen(tags=tags, limit=1,PID=int) # this causes a problem if the pages for a specific tab are not above or equal to the supplied integer. Too bad!
    wr = xmlparse(xurl)
    return wr



def rprefix(str, r): 
    rstr = str.replace(r,"")
    return rstr

bot = commands.Bot(command_prefix='$')
client = discord.Client() # define our client

@client.event # an event to print on ready
async def on_ready():
    print("Logged in as {0.user}".format(client))
    
@client.event # event that listens for message that contains our prefix and a command
async def on_message(message):
    if message.author == client.user:
        return
    # prints the message into our console
    print(message.content)

    if message.content.startswith('$porn'): # we have to do this in a really stupid manner
        tags = rprefix(message.content, '$porn')
        answer = r34dl(tags,random.randint(1,100))
        await message.channel.send(answer + 'made by jess#0101')


# @bot.command() # this doesn't work. Why? no clue. So we're going to have to do this the hard way.
# async def test(ctx, arg):
#     await ctx.say(arg)


# since this is a very private bot im going to censor this on the github
# runs the bot
client.run('enter token here')

# @bot.command()
# async def porn(ctx, args):
#     # use our func for rule34 polling
#     print(r.URLGen(args, limit=1))
#     answer = r34dl(args)
#     print (r34dl(args))
#     await ctx.send(answer)
# deprecated method because @bot.command() isn't working right now
# feel free to make some commits
