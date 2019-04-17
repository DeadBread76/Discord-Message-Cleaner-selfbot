import discord
import asyncio
import json
import sys
import time

client = discord.Client()
with open('config.json', 'r') as handle:
    config = json.load(handle)
    token = (config["token"])
    if token == "Token_Here":
        print ("You Haven't set up the config.json. Please set it up and then run the program again.")
        time.sleep(5)
        sys.exit()
    cleanphrase = (config["cleanphrase"])
    print ("Logging in with token: " + str(token))
    print ("The selected cleanphrase is " + str(cleanphrase))

@client.event
async def on_ready():
    print ('Logged in as')
    print (client.user.name)
    print (client.user.id)
    print ('--------------------')
    print ('Type "' + str(cleanphrase) + '" in the channel you want to clean.')

@client.event
async def on_message(message):
    counter = 0
    if message.content.startswith(str(cleanphrase)) and message.author == client.user:
        async for message in message.channel.history(limit=99999):
            if message.author == client.user:
                await message.delete()
                counter += 1
        msg = "✅`Cleaned " + str(counter) + " messages.`"
        end = await message.channel.send(msg)
        await asyncio.sleep(1)
        await end.delete()

client.run(token, bot=False)
