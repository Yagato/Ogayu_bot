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

    if message.content.startswith("$ogayu"):
        with open('res/ola_okayu.png', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)

    if message.content.startswith("$sui"):
        with open('res/ola_suisei.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channels.end(file=picture)
    
    if "mucho texto" in message.content:
        with open('res/mucho_texto.mp4', 'rb') as f:
            picture = discord.File(f)
            await message.reply(file=picture)

load_dotenv()
client.run(os.getenv('TOKEN'))