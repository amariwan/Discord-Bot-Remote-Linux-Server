import discord
import os

client = discord.Client()
sudoPassword = 'Your Pass'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.content == '{0.content}'.format(message):
            command = '{0.content}'.format(message)
            output = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
            await message.channel.send(output)

client = MyClient()

client.run('Your TOKEN')
