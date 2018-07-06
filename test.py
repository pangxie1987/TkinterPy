from tkMessageBox import showinfo
from Tkinter import *
from tkinter import ttk
# showinfo('info','Message:')

def changeitems():
    print(cnames.get())
    tnames = 'python', 'TCL', 'ruby', 'java'
    cnames.set(tnames)

top = Tk()
top.geometry('300x600')
top.minsize(400,200)
top.title('StringVar')

tnames = ('python', 'TCL', 'ruby')
cnames = StringVar(top)
cnames.set(tnames)

lis = Listbox(top, listvariable=cnames, height=10).pack()
ttk.Button(top, text='submit', command=changeitems).pack()

top.mainloop()
