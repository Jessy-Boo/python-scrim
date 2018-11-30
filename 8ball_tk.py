import random
from tkinter import *

window = Tk()
window.title("Magic 8-Ball")
window.geometry('295x60')

magics = ['It is certain','It is decidedly so','Without a doubt','Yes - definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy, try again','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again','Don\'t count on it','My reply is no','My sources say no','Outlook not so good','Very doubtful']
def clicked(event):
	magicn = random.randint(0,19)
	res = magics[magicn] + ' \n '# + txt.get()
	lbl.configure(text=res)
window.bind('<Return>', clicked)

txt = Entry(window, width=30)
txt.grid(column=0, row=1, columnspan=3)

lbl = Label(window, text="What will you ask the magic 8-ball?\n", cursor="star")
lbl.grid(column=0, row=0, columnspan=2)

btn = Button(window, text="Ask", command=clicked)
btn.grid(column=4,row=1)

window.mainloop()