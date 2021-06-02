from tkinter import *

top = Tk()
top.geometry("200x250")  

mb =  Menubutton ( top, text = "gfg",relief = FLAT)
mb.grid()
mb.menu  =  Menu ( mb, tearoff = 0 )
mb['menu']  =  mb.menu
cVar  = IntVar()
aVar = IntVar()
mb.menu.add_checkbutton ( label ='Contact', variable = cVar )
mb.menu.add_checkbutton ( label = 'About', variable = aVar )
mb.pack()



top.mainloop()