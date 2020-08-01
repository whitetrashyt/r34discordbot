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
    # prints the message into our console for debug
    print(message.content)

    if message.content.startswith('$porn'): # since discord.ext isn't working, we'll have to use a very unorthodox method
        tags = rprefix(message.content, '$porn')
        answer = r34dl(tags,random.randint(1,100))
        await message.channel.send(answer + 'made by jess#0101')




# logs in to the bot
client.run('enter token here')

