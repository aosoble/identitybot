import sys
import os
import discord
import asyncio
from introduction import Introduction
from logger import StreamToLogger, redirectOutputToLog

redirectOutputToLog()

client = discord.Client()

CLIENT_TOKEN = os.environ['CLIENT_TOKEN']

@client.event
async def on_ready():
    print('Identity Bot is now online')

@client.event
async def on_message(message):
    if message.content.startswith('!id '):
        introduction = Introduction()
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
        elif command.startswith('help'):
            client.send_message(message.author, """
            `iam [introduction]`: This command will save your whatever you set as [introduction] with the bot. Your introduction can be as long as you want. Other users can get your introduction using the command below.\n
            `whois @user1 @user2`: This command will get introductions for the users you mention in the message and DM them to you. Note that it sends a DM and does not reply on the same channel.\n
            `list`: This command lists all users who have saved introductions with Identity Bot on your server.\n
            `delete`: This command will delete your introduction. Other users won't be able to get your introduction any more after using this command.\n
            `help`: Displays this help message.
            """)

client.run(CLIENT_TOKEN)
