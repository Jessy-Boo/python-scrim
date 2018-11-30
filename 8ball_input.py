import os
import random
def clear(): #This smooths the experience down
	os.system('cls||clear')
def magic():
	print(magicq + "\n.............\n" + magics[magicn])
magicn = random.randint(0,20)
magics = ['It is certain','It is decidedly so','Without a doubt','Yes - definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy, try again','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again','Don\'t count on it','My reply is no','My sources say no','Outlook not so good','Very doubtful']
clear()
magicq = input("The magic 8-ball answers any yes/no question you throw at it.\n\nWhat will you ask the 8-ball?\n\n")
clear()
magic()