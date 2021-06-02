from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)


Label(master, text='First Name').grid(row=2)
Label(master, text='Last Name').grid(row=3)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=2, column=1)
e2.grid(row=3, column=1)

root = Tk()
#frame = Frame(root,highlightcolor='red',bg='green',width=200,height=200)
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
redbutton = Button(frame, text = 'Red', fg ='red')
redbutton.pack( side = LEFT)
greenbutton = Button(frame, text = 'Green', fg='green')
greenbutton.pack( side = LEFT )
bluebutton = Button(frame, text ='Blue', fg ='blue')
bluebutton.pack( side = RIGHT )

blackbutton = Button(bottomframe, text ='Black', fg ='black')
blackbutton.pack( side = BOTTOM)

#root = Tk()
w = Label(bottomframe, text='GeeksForGeeks.org!')
w.pack()

mainloop()