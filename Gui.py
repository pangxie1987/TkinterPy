# -*- coding:utf-8 -*-
'''
偏函数partial的使用
'''

from functools import partial
import Tkinter

root = Tkinter.Tk()
MyButton = partial(Tkinter.Button, root, fg='white', bg='blue')
b1 = MyButton(text='Button1')
b2 = MyButton(text='Button2')
qb = MyButton(text='Quit', bg='red', command=root.quit)

qb.pack(fill=Tkinter.X, expand=True)
root.title('PFAs')
root.mainloop()

