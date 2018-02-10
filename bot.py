import discord
import asyncio
import json
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


        if message.content.startswith("::enable everyone"):

                data = json.load(open("prefs.json"))
                value = data[str(message.server)]["everyone_disabled"]
                data[str(message.server)]["everyone_disabled"] = True
                with open("prefs.json", "w") as output:
                        json.dump(data, output)

                if value == True:
                        mymessage = await client.send_message(message.channel, "```the use of @everyone is already forbidden in %s```" % (str(message.server)))
                        await client.delete_message(message) #deletes command
                        await asyncio.sleep(5)
                        await client.delete_message(mymessage) #deletes confirmation message
                else:
                        mymessage = await client.send_message(message.channel, "```the use of @everyone is now forbidden in %s```" % (str(message.server))) #sends confirmation message
                        await client.delete_message(message) #deletes command
                        await asyncio.sleep(5)
                        await client.delete_message(mymessage) #deletes confirmation message

        if message.content.startswith("::disable everyone"):

                data = json.load(open("prefs.json"))
                value = data[str(message.server)]["everyone_disabled"]
                data[str(message.server)]["everyone_disabled"] = False
                with open("prefs.json", "w") as output:
                        json.dump(data, output)

                if value == False:
                        mymessage = await client.send_message(message.channel, "```the use of @everyone is already permitted in %s```" % (str(message.server)))
                        await client.delete_message(message) #deletes command
                        await asyncio.sleep(5)
                        await client.delete_message(mymessage) #deletes confirmation message
                else:
                        mymessage = await client.send_message(message.channel, "```the use of @everyone is now permitted in %s```" % (str(message.server))) #sends confirmation message
                        await client.delete_message(message) #deletes command
                        await asyncio.sleep(5)
                        await client.delete_message(mymessage) #deletes confirmation message

        if message.mention_everyone: #deletes any message that contains the string @everyone
<<<<<<< HEAD
                
                data = json.load(open("prefs.json"))
                if data[str(message.server)]["everyone_disabled"] == True:

                        mymessage = await client.send_message(message.channel, "```@everyone is disabled on this server```") #sends warning message
                        await client.delete_message(message) #deletes the message containing @everyone
                        await asyncio.sleep(5)
                        await client.delete_message(mymessage) #deletes the warning message after 5 seconds
               

        if message.content.startswith("::enable filter"):

                data = json.load(open("prefs.json"))
                value = data[str(message.server)]["prof_disabled"]
                data[str(message.server)]["prof_disabled"] = True
                with open("prefs.json", "w") as output:
                        json.dump(data, output)

                if value == True:
                        mymessage = await client.send_message(message.channel, "```the use of profanity is already forbidden in %s```" % (str(message.server)))
                        await client.delete_message(message) #deletes command
                        await asyncio.sleep(5)
                        await client.delete_message(mymessage) #deletes confirmation message
                else:
                        mymessage = await client.send_message(message.channel, "```the use of profanity is now forbidden in %s```" % (str(message.server))) #sends confirmation message
                        await client.delete_message(message) #deletes command
                        await asyncio.sleep(5)
                        await client.delete_message(mymessage) #deletes confirmation message

        if message.content.startswith("::disable filter"):

                data = json.load(open("prefs.json"))
                value = data[str(message.server)]["prof_disabled"]
                data[str(message.server)]["prof_disabled"] = False
                with open("prefs.json", "w") as output:
                        json.dump(data, output)

                if value == False:
                        mymessage = await client.send_message(message.channel, "```the use of profanity is already permitted in %s```" % (str(message.server)))
                        await client.delete_message(message) #deletes command
                        await asyncio.sleep(5)
                        await client.delete_message(mymessage) #deletes confirmation message
                else:
                        mymessage = await client.send_message(message.channel, "```the use of profanity is now permitted in %s```" % (str(message.server))) #sends confirmation message
                        await client.delete_message(message) #deletes command
                        await asyncio.sleep(5)
                        await client.delete_message(mymessage) #deletes confirmation message

        stripped = "".join([x for x in message.content if ord(x) < 128]).lower()
        if any([word in stripped for word in profs]): #deletes any message that contains profanity
                
                data = json.load(open("prefs.json"))
                if data[str(message.server)]["prof_disabled"] == True:

                        mymessage = await client.send_message(message.channel, "```profanities are not allowed on this server```") #sends warning message
                        await client.delete_message(message) #deletes the message containing profanity
                        await asyncio.sleep(5)
                        await client.delete_message(mymessage) #deletes the warning message after 5 seconds
                        
        stripped = "".join([x for x in message.content if ord(x) < 128]).lower()
        if any([word in stripped for word in profs]): #deletes any message that contains profanity
                mymessage = await client.send_message(message.channel, "```profanities are not allowed on this server```")
                await client.delete_message(message)
                await asyncio.sleep(5)
                await client.delete_message(mymessage)
>>>>>>> 6f370bd9b6badd2e9a5c741acf43033caa2f7d6b

client.run(tok)
