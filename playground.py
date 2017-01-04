from Tkinter import * #gives us access to everything in the Tkinter class

root = Tk() #gives us a blank canvas object to work with
root.title("MWales_First GUI Program with Tkinter")

button1 = Button(root, text="button1")
button1.grid(row=1, column=1)

entry1 = Entry(root)
entry1.grid(row=1, column=0)

label1 = Label(root, text="Hello World", bg="purple")
label1.grid(row=0, column=0, sticky=EW)

mainloop() #causes the windows to display on the screen until program closes