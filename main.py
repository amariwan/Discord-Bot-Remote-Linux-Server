import discord
import subprocess
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Set up the Discord client
client = discord.Client()

# Retrieve sensitive information from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')
sudo_password = os.getenv('SUDO_PASSWORD')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        # Ignore messages from the bot itself
        if message.author == self.user:
            return
        
        # Check if the message starts with a specific command prefix
        if message.content.startswith('!execute '):
            command = message.content[len('!execute '):].strip()

            try:
                # Execute the command using subprocess
                result = subprocess.run(
                    ['sudo', '-S'] + command.split(),
                    input=f'{sudo_password}\n',
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )

                # Prepare output message
                output = result.stdout + result.stderr
                response = f'```bash\n{output}\n```'

                # Send the response back to the channel
                await message.channel.send(response)
            
            except Exception as e:
                await message.channel.send(f'Error executing command: {str(e)}')

# Start the bot with the provided token
client = MyClient()
client.run(TOKEN)
