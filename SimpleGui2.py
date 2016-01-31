#This gui allows you to add strings to a sqlite dataBase, while at the same time, opening it ina browser

import sys
from tkinter import *
import webbrowser
import sqlite3

#Create and establish connection:

conn = sqlite3.connect('db73.db')

#creating Table
def database_Table():
    conn.execute("CREATE TABLE if not exists \
    CONTENT_STORAGE1(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    CONTENT BLOB);")


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

#Inserting into the DB:

def insertDB():
    conn = sqlite3.connect('db73.db')
    c = conn.cursor()
    content = ment.get()
    c.execute("INSERT INTO CONTENT_STORAGE1 (content) VALUES (?)", (content,))
    conn.commit()
    
#This next def allows you to run the three defs simulteneously

def buttonMagic():
    database_Table()
    insertDB()
    txtToBrowsr()   

#Here is were we create the gui and the variable.      

mGui = Tk()
ment = StringVar()

mGui.geometry('450x450+500+300')
mGui.title("Brook's Gui Helper")

blabel = Label(mGui, text='Web Browser').pack()

bbutton = Button(mGui, text = 'Print', command = textInput, fg = 'blue', bg='yellow').pack()

bbutton1 = Button(mGui, text = 'Achieve Desired Result', command = buttonMagic, fg = 'yellow', bg='blue').pack()

bEntry = Entry(mGui, textvariable=ment, width=50)
bEntry.pack(height)
