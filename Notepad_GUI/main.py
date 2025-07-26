from tkinter import *
from tkinter import filedialog


def save_file():
    open_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if open_file is None:
        return
    text=str(field_entry.get(1.0, END))
    open_file.write(text)
    open_file.close()


def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('text file', '.txt')])
    if file is not None:
        content = file.read()
    field_entry.insert(INSERT, content)


root = Tk()
root.geometry('600x600')
root.title('Notepad')
root.config(bg='lightblue')
root.resizable(False, False)

save_button = Button(root, width='20', height='2', bg='#fff', text='Save File', command=save_file).place(x=100, y=5)
save_button = Button(root, width='20', height='2', bg='#fff', text='Open File', command=open_file).place(x=300, y=5)

field_entry = Text(root, height='33', width='72', wrap=WORD)
field_entry.place(x=10, y=60)


root.mainloop()
