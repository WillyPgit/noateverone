import discord
import asyncio
import random
import pickle
import os
from tendo import singleton
from profanities import profs
from token1 import tok

me = singleton.SingleInstance()
client = discord.Client()

@client.event
async def on_ready(): #prints log in info
        print("Logged in as")
        print(client.user.name)
        print(client.user.id)

@client.event
async def on_message(message):
        if message.mention_everyone: #deletes any message that contains the string @everyone
                await client.send_message(message.channel, "\\@everyone is disabled on this server")
                await client.delete_message(message)

        stripped = "".join([x for x in message.content if ord(x) < 128]).lower()
        if any([word in stripped for word in profs]): #deletes any message that contains profanity
                await client.send_message(message.channel, "profanities are not allowed on this server")
                await client.delete_message(message)

client.run(tok)
