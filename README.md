# r34discordbot
A discord bot that pulls images from rule34 with specific tags and posts them.


Feel free to use it.

# Requirements
Python 3.8

# Usage
There are two ways to use this:
1. As a discord bot
2. Through your terminal
your terminal way will only supply you with a link, your discord bot will post it in your server.
Here's the instructions, of course.
### As a discord bot:
1. Download the file (`git clone https://github.com/whitetrashyt/r34discordbot/`or use the releases page)
2. Grab your discord bot token (If you dont know how, check out [Discord's developer page](https://discord.com/developers/applications))
3. Edit the main.py file to find line 70, `client.run('enter token here')`, copy paste your token there.
4. run main.py, either through your terminal (`py main.py`), or by double clicking on it.
5. In your discord server (With your bot invited,) do $help
6. have fun, you loser.
### Through your terminal:
1. Open your console (Command prompt or Terminal, what have you.)
2. Navigate to the folder which the .py file is located
3. run either through `py r34discordbot.py -t <tags>` or `r34discordbot.py -t <tags>`

`-t` supplies your tags for the rule34 search, for example, `-t furry sound`
There is actively no special character filter, so if you were to enter `-t furry,sound` your query would be denied. Only use spaces.

# Credits
Thanks to [LordOfPolls](https://github.com/LordOfPolls) for his [Rule34-api-wrapper](https://github.com/LordOfPolls/Rule34-API-Wrapper) (It made my job semi easier and also much more difficult)

Thanks to Marloes for the help with debugging and stuff, i had some problems along the way and their feed back was definitely helpful!
