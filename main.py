import os
import discord
import requests
import json
import random
#create an instance of client
client = discord.Client()

sad_words = ["sad","unhappy","hard","dipressed", "low", "lonely", "angry", "misserable","dipressing", "lost", "lack", "tired"]

starter_motivations = [
  "Cheer up!","Dont be sad!", "All is gonna be well", "You are going to pass through this!","God loves you remember"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")

  json_data = json.loads(response.text)

  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

#register an event
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
    
  msg = message.content

  if message.content.startswith('Hello'):
    await message.channel.send('Hello dear! Let me inspire you today')

  if message.content.startswith('Inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_motivations))
  

client.run(os.getenv('TOKEN'))
  