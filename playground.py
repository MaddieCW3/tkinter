from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox
from PIL import Image, ImageTk
from datetime import date, datetime
from threading import *

def buttonpress():
    entrytxt = entry1.get()
    print entrytxt
    tkMessageBox.showinfo("Here's what you typed", entrytxt)
    
def addtolist():
    entrytxt = entry1.get()
    if check4dup() == False:
        listbox1.insert(END, entrytxt)
        findsize()
    entry1.delete(0,END)
        
def addtolist2(event):
    entrytxt = entry1.get()
    if check4dup() == False:
        listbox1.insert(END, entrytxt)
        findsize()
    entry1.delete(0,END)
    
def clearlist(event):
    listbox1.delete(0, END)
    findsize()
    
def check4dup():
    names = listbox1.get(0, END)
    if entry1.get() in names:
        return True
    else:
        return False
        
def openFileR():
    clearlist1()
    f = open("Readme.txt", "r")
    for line in f:
        name = line[0:-1]
        listbox1.insert(END, name)
    f.close()
    findsize()
    
def openFileW():
    f = open("Readme.txt", 'w')
    names = listbox1.get(0, END)
    for i in names:
        f.write(i+"\n")
    f.close()
        
def findsize():
    label1.config(text=listbox1.size())
    
def clearlist1():
    listbox1.delete(0, END)
    findsize()
    
d = datetime.now()
y = d.year
h = d.hour

def generate():
    while(1):
        print "Hello"
        
thread1 = Thread(target=generate)
#thread1.start()

#generate()

root = Tk() #gives us a blank canvas object to work with
root.title("MWales_First GUI Program with Tkinter")

button1 = Button(root, text="button1", command=addtolist)
button1.grid(row=1, column=1)

entry1 = Entry(root)
entry1.grid(row=1, column=0)
entry1.bind("<Return>", addtolist2)

label1 = Label(root, text="Hello World", bg="purple", anchor=W)
label1.grid(row=0, column=0, sticky=EW, columnspan=3)

scrollbar = Scrollbar(root, orient=VERTICAL)
listbox1 = Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox1.yview)
scrollbar.grid(row=2, column=2, rowspan=10, sticky=NS)
listbox1.grid(row=2, column=0, columnspan=2, sticky=EW)
listbox1.bind("<Button-3>", clearlist)

listbox1.insert(END, "Harry")
listbox1.insert(END, "Ron")
listbox1.insert(END, "Hermione")

findsize()

image = Image.open("ball.jpg")
image = image.resize((100,100))
photo = ImageTk.PhotoImage(image)

label2 = Label(image=photo)
label2.image = photo #keep a reference!
label2.grid(row=12, column=0)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openFileR)
filemenu.add_separator()
filemenu.add_command(label="Save", command=openFileW)

menubar.add_cascade(label="file", menu=filemenu)

root.config(menu=menubar)

mainloop() #causes the windows to display on the screen until program closes