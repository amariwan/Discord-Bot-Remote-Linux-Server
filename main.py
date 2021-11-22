import discord
import os
import subprocess

client = discord.Client()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.content == '{0.content}'.format(message):
            output = subprocess.getoutput('{0.content}'.format(message))
            await message.channel.send(output)

client = MyClient()

client.run('Your TOKEN')
