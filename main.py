import os
import discord
import requests
import json
#create an instance of client
client = discord.Client()

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

  if message.content.startswith('Hello'):
    await message.channel.send('Hello dear! Let me inspire you today')

  if message.content.startswith('Inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  

client.run(os.getenv('TOKEN'))
  