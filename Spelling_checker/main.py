from tkinter import *
from textblob import TextBlob


def check_spelling():
    message = entry_text.get()
    text = TextBlob(message)
    right = text.correct()

    correct_spelling = Label(root, text='Correct spelling is: ', font=('poppins', 20), bg='#dae6f6', fg='#364971')
    correct_spelling.place(x=100, y=250)
    spell.config(text=right)


root = Tk()
root.title('Spelling Checker')
root.geometry('700x400')
root.config(bg='#dae6f6')

heading = Label(root, text='Spelling Checker', font=('Trebuchet MS', 30, 'bold'), bg='#dae6f6', fg='#364971')
heading.pack(pady=(50, 0))

entry_text = Entry(root, justify='center', width=30, font=('poppins', 25), bg='white', border=2)
entry_text.pack(pady=10)
entry_text.focus()

button = Button(root, text='Check', font=('Arial', 20, 'bold'), fg='white', bg='red', command=check_spelling)
button.pack()

spell = Label(root, font=('poppins', 20), bg='#dae6f6', fg='#364971')
spell.place(x=350, y=250)

root.mainloop()

