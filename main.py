import discord
import os
import time
import random
#import vexpy as vp
import wikipedia


timeRn = time.time()




bot = discord.Client()

def Search(arg):
    search = wikipedia.summary(arg, sentences=2)
    return search
    print(search)






  
## these are all the lists i use in this bot ##

eight_ballanswers = ['yes','no','go with what your heart says','maybe','ask again tomorrow','it is so',"i'm not so sure"]

quotes = ["We cannot solve problems with the kind of thinking we employed when we came up with them.", "Learn as if you will live forever, live like you will die tomorrow.","Stay away from those people who try to disparage your ambitions. Small minds will always do that, but great minds will give you a feeling that you can become great too.","When you give joy to other people, you get more joy in return. You should give a good thought to happiness that you can give out.","When you change your thoughts, remember to also change your world.","It is only when we take chances, when our lives improve. The initial and the most difficult risk that we need to take is to become honest.","Nature has given us all the pieces required to achieve exceptional wellness and health, but has left it to us to put these pieces together."]

games = ['Minecraft', 'ROBLOX','Kerbal Space Program', 'Endless Sky', 'Red Dead Redemption', 'War Thunder']

videos = ['Stranger Things', 'Madascagar 2','Planes','SpaceX Launches']

gifs = ['http://imgur.com/gallery/YiMUiop','https://media3.giphy.com/media/iLJ9lXuIihOiOuJ5ry/giphy.gif','https://imgur.com/gallery/zW1B6','https://imgur.com/gallery/vjHg7lX','https://imgur.com/gallery/5ZQMwtP','https://imgur.com/gallery/k59TCHf']
# 6, 0-5

images = ['https://imgur.com/gallery/c1D3W','https://imgur.com/gallery/WnfH3','https://imgur.com/gallery/jluCLzA','https://imgur.com/gallery/gFhGNWP','https://imgur.com/gallery/eKZTF']
# 5, 0-4

CQ_images = ['https://cdn.motor1.com/images/mgl/6MGkl/s1/bugatti-chiron-pur-sport.webp','https://api.ferrari.com/cms/network/medias//resize/6093c2680abef6224c06a042-ferrari-magazine-oGehKAJD4w.jpg?apikey=9QscUiwr5n0NhOuQb463QEKghPrVlpaF','https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2021-chevrolet-corvette-stingray-coupe-2lt-z51-ltintro-161-1635859600.jpg?crop=0.726xw:0.817xh;0.171xw,0.144xh&resize=640:*','https://upload.wikimedia.org/wikipedia/commons/2/23/2018_McLaren_720S_V8_S-A_4.0.jpg','https://www.rolls-roycemotorcars.com/content/dam/rrmc/marketUK/rollsroycemotorcars_com/3-4-ghost/page-properties/rolls-royce-discover-ghost-extended-share-image.jpg','https://media.drivingelectric.com/image/private/s--xk5AR6pz--/v1597784733/drivingelectric/2019-08/1-tesla-model-s.jpg','https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/facelift_2019/model_gw/aventador/2021/gate_aven_s_01_m.jpg','https://upload.wikimedia.org/wikipedia/commons/5/52/BMW_G30_FL_IMG_5351.jpg','https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2019-mercedes-benz-a220-4matic-108-1544471119.jpg?crop=0.675xw:0.505xh;0.0442xw,0.464xh&resize=640:*','https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2020-volvo-xc90-t8-inscription-109-1595600860.jpg?crop=0.769xw:0.577xh;0.106xw,0.250xh&resize=1200:*','https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2022-infiniti-qx80-02-source-1629398719.jpg','https://www.motortrend.com/uploads/2021/11/2022-Jaguar-XF-R-Dynamic_Black_Front_3-4_250821.jpg','https://www.vw.com/content/dam/onehub_pkw/us/en/homepage/models/VW_NGW6_Homepage_Vehicle_Small-2_new.jpg']
# 13, 0-12

CQ_answers = ['bugatti','ferrari','corvette','mclaren','rolls royce','tesla','lamborghini','bmw','mercedes','volvo','infinity','jaguar','volkswagen']
# 13, 0-12


 

@bot.event
async def on_ready():
  print("We have logged in as {0.user}".format(bot))

  ## This gives the bot a random status every time it joins ##
  
 
  gamesVvideos = random.randint(0,1)
  if gamesVvideos == 0:
    whatgame = random.randint(0,5)
    gameStatus = games[whatgame]
    await bot.change_presence(activity=discord.Game(name=gameStatus))


  if gamesVvideos == 1:
    whatvideo = random.randint(0,3)
    videoStatus = videos[whatvideo]
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=videoStatus))

@bot.event
async def on_message(message):
  if message.content == '!hello':
    await message.channel.send('Sup')

  if message.content == '!quote':
    
    quoteIndex = random.randint(0,6)
    quoteSelected = quotes[quoteIndex]
    await message.channel.send(quoteSelected)

  if message.content.startswith('!8ball'):
    ansIndex = random.randint(0,6)
    ansSelected = eight_ballanswers[ansIndex]
    await message.channel.send(ansSelected)

  

  if message.content.startswith('!simonsays') and message.author != bot:
    message_txt = message.content
    message_txt2 = message_txt.replace("!simonsays","")
    await message.channel.send(message_txt2)

  if message.content == '!meme':
    imgIndex = random.randint(0,4)
    imgSelected = images[imgIndex]
    await message.channel.send(imgSelected)

  if message.content == '!gif':
    gifIndex = random.randint(0,5)
    gifSelected = gifs[gifIndex]
    await message.channel.send(gifSelected)

  if message.content == '!carquiz':

    ctx = message.channel
    await ctx.send('Type in the brand of the car that is shown below (all lowercase)')
    quizIndex = random.randint(0,12)
    qSelected = CQ_images[quizIndex]
    aSelected = CQ_answers[quizIndex]
    await ctx.send(qSelected)
    print(qSelected)
    print(aSelected)
    
    action = await bot.wait_for('message')
    print(action.content)
    user = action.author.name
    if action.content == aSelected:
      await ctx.send(f"Correct, good job {user}")
    else:
      await ctx.send(f"That is incorrect {user}, the answer is **{aSelected}**")

  if message.content == '!help':
    ctx = message.channel
    ctx.send("List of commands: (!hello: bot replies with sup), (!quote: bot gives you a random quote), (!8ball {question}: will give you a randomized answer), (!simonsays {text}: bot will repeat {text} back to you), (!meme: generates a random breaking bad meme), (!gif: generates a random breaking bad gif), (!carquiz: quizzes your knowledge of car brands)")

      

    
      

bot.run(os.getenv('TOKEN'))
