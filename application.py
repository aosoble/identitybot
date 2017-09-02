import sys
import os
import discord
import asyncio
from introduction import Introduction
from logger import StreamToLogger, redirectOutputToLog

redirectOutputToLog()

client = discord.Client()
introduction = Introduction()

CLIENT_TOKEN = os.environ['CLIENT_TOKEN']

@client.event
async def on_ready():
    print('Identity Bot is now online')

@client.event
async def on_message(message):
    raise Exception("Some exception")
    if message.content.startswith('!id '):
        command = message.content[4:]
        if command.startswith('iam '):
            intro = command[4:]
            user = message.author
            server = user.server
            introduction.newIntroduction(server.id,user.id,intro)
            await client.send_message(message.author, "Your introduction is now registered with me.")           
        elif command.startswith('whois '):
            server = message.author.server
            for user in message.mentions:
                intro = introduction.getIntroduction(server.id,user.id)
                if intro:
                    await client.send_message(message.author, "Introduction of %s\n\n%s"%(user.name,intro,))
                else:
                    await client.send_message(message.author, "Cannot find introduction for %s"%(user.name,)) 
        elif command.startswith('list'):
            server = message.author.server
            users = introduction.listIntroducedUsers(server.id)
            if users:
                response = "I can show you introductions for the following users:\n\n"
                for user in users:
                    response += "<@%s>" % (user,)
            else:
                response = "No other users have registered introductions with me for this server. You can be the first."
            await client.send_message(message.author, response)
        elif command.startswith('delete'):
            user = message.author
            server = user.server
            introduction.deleteIntroduction(server.id,user.id)
            await client.send_message(message.author, "Your introduction has now been deleted.")

client.run(CLIENT_TOKEN)