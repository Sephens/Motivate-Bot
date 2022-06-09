import os
import discord
import requests
import json
import random

#imports for replit db usage
from replit import db
#create an instance of client
client = discord.Client()

sad_words = ["sad","unhappy","hard","dipressed", "low", "lonely", "angry", "misserable","dipressing", "lost", "lack", "tired"]

starter_motivations = [
  "Cheer up!","Dont be sad!", "All is gonna be well", 
  "You are going to pass through this!",
  "God loves you remember"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")

  json_data = json.loads(response.text)

  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_motivations(motivating_nessages):
  if "motivations" in db.keys():
    motivations = db["motivations"]
    motivations.append(motivating_nessages)
    #save to database
    db["motivations"] = motivations

  else:
    db["motivations"] = [motivating_nessages]


#function to delete a motivating message from the db
def delete_motivation(index):
  #get the list of motivations from the db
  motivations = db["motivations"]
  if len(motivations) > index:
    del motivations[index]
    #save into the db again
    db["motivations"] = motivations

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

  options = starter_motivations
  if "motivations" in db.keys():
    options = options + db["motivations"]


  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    motivating_message = msg.split("$new ",1)[1]
    update_motivations(motivating_message)
    await message.channel.send("New motivating message added")

  if msg.startswith("$del"):
    motivations = []
    if "motivations" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_motivation(index)
      motivations = db["motivations"]
    await message.channel.send(motivations)
      
    
client.run(os.getenv('TOKEN'))
  