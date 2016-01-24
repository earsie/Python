#This is a simple gui that allows you to input text into a text-box, display it on the gui, and also open it into a browser.

import sys
from tkinter import *
import webbrowser

#This is a def for inputting the value of 'ment' below, into a variable "mtext", remember the .get method gets and stores info.
def textInput():
    btext = ment.get()
    blabel2 = Label(mGui, text=btext).pack()

#As it states here, this takes what was stored in the 'ment' variable below and uses the open in browser..named sample.html

def txtToBrowsr():
    f=open('sample.html', 'w')
    message = ment.get()
    f.write(message)
    f.close()
    webbrowser.open_new_tab('sample.html')
       

#Here is were we create the gui and the variable.      

mGui = Tk()
ment = StringVar()

mGui.geometry('450x450+500+300')
mGui.title("Brook's Gui Helper")

blabel = Label(mGui, text='Web Browser').pack()

bbutton = Button(mGui, text = 'Print', command = textInput, fg = 'blue', bg='yellow').pack()

bbutton1 = Button(mGui, text = 'Open In Browser', command = txtToBrowsr, fg = 'yellow', bg='blue').pack()

bEntry = Entry(mGui, textvariable=ment).pack()

