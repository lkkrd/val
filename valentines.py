from tkinter import *
import random

root = Tk()
rejections = 0
questions = 0
bbywords = ['bby', 'bbyyyy', 'skarbie', 'słońce',
            'słońceee', 'honeyyy', 'honeybunnn', 'BBYYY']


def choose():
    whatbtn.destroy()
    question.config(text='Will you be my valentine?')
    yesbtn.pack()
    nobtn.pack()


def ask():
    global questions
    questions += 1
    print(questions)
    while questions < 7:
        if question.cget('text') == 'BBYYY':
            choose()
            return
        x = random.choice(bbywords)
        question.config(text=x)
        return
    choose()
    return


question = Label(root, text='Bby?')
whatbtn = Button(root, text='what', padx=50, command=ask)
yesbtn = Button(root, text='Yes', padx=40)
nobtn = Button(root, text='No', padx=40)

question.pack()
whatbtn.pack()

root.mainloop()
