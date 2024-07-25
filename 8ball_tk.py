import random
from tkinter import *

window = Tk()
window.title("Magic 8-Ball")
window.geometry('400x200')

magics = [
    'It is certain', 'It is decidedly so', 'Without a doubt', 'Yes - definitely',
    'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good',
    'Yes', 'Signs point to yes', 'Reply hazy, try again', 'Ask again later',
    'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
    'Don\'t count on it', 'My reply is no', 'My sources say no',
    'Outlook not so good', 'Very doubtful'
]

def clicked(event=None):
    magicn = random.randint(0, len(magics) - 1)
    res = magics[magicn]
    lbl_result.config(text=res)

frame = Frame(window, padx=20, pady=20)
frame.pack(expand=True)

lbl_question = Label(frame, text="What will you ask the magic 8-ball?", font=("Arial", 14))
lbl_question.grid(row=0, column=0, columnspan=2, pady=10)

txt_question = Entry(frame, width=40, font=("Arial", 12))
txt_question.grid(row=1, column=0, columnspan=2, pady=5)
txt_question.bind('<Return>', clicked)

btn_ask = Button(frame, text="Ask", command=clicked, font=("Arial", 12))
btn_ask.grid(row=2, column=0, columnspan=2, pady=10)

lbl_result = Label(frame, text="", font=("Arial", 14), fg="red")
lbl_result.grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()
