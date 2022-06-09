import os
#import discord 
import discord
#import for http requests from API
import requests
import json
import random
from replit import db
#create an instance of client
client = discord.Client()

sad_words = ["sad","unhappy","hard","dipressed", "low", "lonely", "angry", "misserable","dipressing", "lost", "lack", "tired"]

starter_motivations = [
  "Cheer up!","Dont be sad!", "All is gonna be well", "You are going to pass through this!","God loves you remember"
]

song_groups = ["RNB","Gospel","HIPHOP", "Reggea" , "Instrumental"]
songs = ["Love me now -John Legend","I wish I knew -Steve Brukes","Bwana ni mwokozi -Jeniffer", "Prisoners of guilt -Lucky Dube"]

if "responding" not in db.keys():
  db["responding"] = True



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
  #check if message is from the user
  if message.author == client.user:
    return
  msg = message.content

  #Bot response
  if db["responding"]:
      if message.content.startswith('Hello'):
        await message.channel.send('Hello dear! Tell me anything')
    
      if message.content.startswith('Sing for me'):
        await message.channel.send('Which is your fav group?')
    
      if any(word in msg for word in song_groups):
        await message.channel.send(random.choice(songs))
    
      if message.content.startswith('Inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    
      if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_motivations))

  #turn the bot on or off
  if msg.startswith("Responding"):
    value = msg.split("Responding ",1)[1]
    if value.lower() == ("true"):
      db["responding"] = True
      await message.channel.send("Response turned on")
    elif value.lower() == ("false"):
      db["responding"] = False
      await message.channel.send("Response is turned off")

  

client.run(os.getenv('TOKEN'))
  