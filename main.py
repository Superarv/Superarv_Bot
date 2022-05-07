import discord
import os
import time
import random


bot = discord.Client()


games = ['Minecraft', 'ROBLOX','Kerbal Space Program', 'Endless Sky', 'Red Dead Redemption', 'War Thunder']

videos = ['Stranger Things', 'Madascagar 2','Planes','SpaceX Launches']


 

@bot.event
async def on_ready():
  print("We have logged in as {0.user}".format(bot))

  ## This gives the bot a random status every 30 minutes ##
  
  while True:
    gamesVvideos = random.randint(0,1)
    if gamesVvideos == 0:
      whatgame = random.randint(0,5)
      gameStatus = games[whatgame]
      await bot.change_presence(activity=discord.Game(name=gameStatus))


    if gamesVvideos == 1:
      whatvideo = random.randint(0,3)
      videoStatus = videos[whatvideo]
      await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=videoStatus))

  time.sleep(1800)
      

 



  

  

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  if message.content.startswith('!hello'):
    await message.channel.send('Sup')

  

  if message.content.startswith('!quote'):
    pass

bot.run(os.getenv('TOKEN'))
