import tkinter as tk
from tkinter import *
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy, bg='red', activebackground='green')
button.pack()

w = Canvas(r, width=40, height=60)
w.pack()
canvas_height=40
canvas_width=200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )



r.mainloop()