# This script is for my <Redacted> bot.
# Simple. Okay?
# Hey, if you're reading my stupid code, may i reccomend a song?
# Check out The lost Battalion, by Sabaton.
# I also have a coding playlist. I listened to it while making this stupid garbage
# https://open.spotify.com/playlist/0I48OWh7mSR7vDssy3nabw?si=47Ug13mKRC6dYEV_Wz6dPA
# sorry if this lil advert bothered you <3


# IMPORTS
import rule34
# Rule34 api wrapper that makes my job easier.
import argparse
# Parses arguments from command lines.
import urllib.request as u
# Used to open xml files online
import xml.etree.ElementTree as et
# Used to parse xml files


# defining the XML parser function
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
testlist = ['hj','hi']   
        # grab the attribute file_url and set it to fileurl for writing to a text doccument
# Define a simple WTT function for interaction with the bot.
# The bot uses JS so the only thing i can really do is read the text file on the JS script and work from there
def wtt(str):
    text_file = open("stuff.txt", "w")
    t = text_file.write(str)
    text_file.close()
# we need a list to string function for later
def lts(org_list, seperator=' '):
    # LTS, list to string.
    return seperator.join(org_list)


# Need to set this like this for asynch calls.
r = rule34.Sync()

# argument parser using python3 argparse module
ap = argparse.ArgumentParser(description='returns url with tag.', prefix_chars='-')
ap.add_argument('-t',dest='tagA',help='specify tags',nargs='+') # i want you to know, dear reader, that this line of code caused me to breakdown into nervous laughter because it was outputting as a list, breaking the whole fucking code.
args = ap.parse_args() # corrected this to properly take the arguments and use them as a variable/string/thing

# Old debug stuff. Kept it in for future use.
# print(args.tagA)
tagf = lts(args.tagA)
# print(tagf)
xurl = r.URLGen(tagf)
wr = xmlparse(xurl) # Parse the XML URL, grabs the necessary attribute.
# print(wr)
# now that the worst bit of this is over, we need to write this to a text file.
wtt(wr)
# easy enough

# Normally, i'd ad my AKOSDEV's watermark, but i couldn't care less tbh.
# Feel free to make a commit to fucking fix this disgusting mess of code.






