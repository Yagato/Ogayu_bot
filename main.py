# Yagato
# 7/5/2022

import discord
import os
from dotenv import load_dotenv

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("$ola"):
        await message.channel.send("Olaaa :wave:")

load_dotenv(os.path.join(os.getcwd(), '.env'))
client.run(os.getenv('TOKEN'))