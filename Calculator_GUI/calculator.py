from tkinter import Tk, Entry, StringVar, Button

class Calculator:
    def __init__(self, master):
        # setup up everything regarding the window
        master.title('Calculator')
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        # setup equation and entry field
        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg='#ccddff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # Calculator buttons config.
        Button(width=11, height=4, text='(', relief='flat', bg='white', command= lambda:self.show('(')).place(x=0, y=50)
        Button(width=11, height=4, text=')', relief='flat', bg='white', command= lambda:self.show(')')).place(x=90, y=50)
        Button(width=11, height=4, text='%', relief='flat', bg='white', command= lambda:self.show('%')).place(x=180, y=50)
        Button(width=11, height=4, text='1', relief='flat', bg='white', command= lambda:self.show(1)).place(x=0, y=125)
        Button(width=11, height=4, text='2', relief='flat', bg='white', command= lambda:self.show(2)).place(x=90, y=125)
        Button(width=11, height=4, text='3', relief='flat', bg='white', command= lambda:self.show(3)).place(x=180, y=125)
        Button(width=11, height=4, text='4', relief='flat', bg='white', command= lambda:self.show(4)).place(x=0, y=200)
        Button(width=11, height=4, text='5', relief='flat', bg='white', command= lambda:self.show(5)).place(x=90, y=200)
        Button(width=11, height=4, text='6', relief='flat', bg='white', command= lambda:self.show(6)).place(x=180, y=200)
        Button(width=11, height=4, text='7', relief='flat', bg='white', command= lambda:self.show(7)).place(x=0, y=275)
        Button(width=11, height=4, text='8', relief='flat', bg='white', command= lambda:self.show(8)).place(x=90, y=275)
        Button(width=11, height=4, text='9', relief='flat', bg='white', command= lambda:self.show(9)).place(x=180, y=275)
        Button(width=11, height=4, text='0', relief='flat', bg='white', command= lambda:self.show(0)).place(x=90, y=350)
        Button(width=11, height=4, text='.', relief='flat', bg='white', command= lambda:self.show('.')).place(x=180, y=350)
        Button(width=11, height=4, text='+', relief='flat', bg='white', command= lambda:self.show('+')).place(x=270, y=275)
        Button(width=11, height=4, text='-', relief='flat', bg='white', command= lambda:self.show('-')).place(x=270, y=200)
        Button(width=11, height=4, text='/', relief='flat', bg='white', command= lambda:self.show('/')).place(x=270, y=50)
        Button(width=11, height=4, text='x', relief='flat', bg='white', command= lambda:self.show('*')).place(x=270, y=125)
        Button(width=11, height=4, text='=', relief='flat', bg='lightblue', command= self.solve).place(x=270, y=350)
        Button(width=11, height=4, text='C', relief='flat', command= self.clear).place(x=0, y=350)
    
    # shows the on gui the char we provided from the buttons
    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    # entry value and equation get erased and start over with nothing
    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    # Takes everythin stored in entry_value and evaluates the operation, the entry gets assigned the value of equation
    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)



root = Tk() # create Tk object
calculator = Calculator(root) # create Calculator object, we pass in Tk object to setup everything within the class
root.mainloop() # keeps the GUI running
