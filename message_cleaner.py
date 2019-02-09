import discord
import asyncio




token = input('Token:')
clientid = input ('Client ID (Your ID):')
client = discord.Client()


@client.event
async def on_ready():
    print ('Logged in as')
    print (client.user.name)
    print (client.user.id)
    print ('--------------------')
    print ('Type "cleanme" in the channel you want to clean.')


@client.event
async def on_message(message):
    if message.content.startswith('cleanme'):
        async for x in client.logs_from(message.channel, limit = 100):
            if x.author.id == (clientid):
                await client.delete_message(x)



client.run(token, bot=False)
