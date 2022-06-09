#Flask is used as the web server
from flask import Flask
#The server wil run on a separate thread from the bot so that they can
#both run at the same time
from threading import Thread


app = Flask('')

@app.route('/')
#the web server will return hello am on to anyone who visits the server
def home():
  return "Hello am ON!"
def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()