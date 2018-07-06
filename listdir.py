

import os
from time import sleep
from Tkinter import *

class DirList(object):
    def __init__(self, initdir=None):
        self.top = Tk()
        self.label = Label(self.top, text='Directory Lister V1.1')
        self.label.pack()
        self.cwd = StringVar(self.top)  # StringVar()跟踪变量的值得变化，以保证值得变更随时可以显示在界面上
        self.dir1 = Label(self.top, fg='blue', font=('Helvetica', 12, 'bold'))
        self.dir1.pack()

        self.dirfm = Frame(self.top)
        self.dirsb = Scrollbar(self.dirfm)
        self.dirsb.pack(side=RIGHT, fill=Y)
        self.dirs = Listbox(self.dirfm, height=15, width=50, yscrollcommand=self.dirsb.set)
        self.dirs.bind('<Double-1>', self.setDirAndGo)  #将回调函数setDirAndGo绑定到事件<Double-1>鼠标双击上
        self.dirsb.config(command=self.dirs.yview)
        self.dirs.pack(fill=BOTH, expand=True)
        self.dirfm.pack(fill=BOTH, expand=True)

        self.dirn = Entry(self.top, width=50, textvariable=self.cwd)
        self.dirn.bind('<Return>', self.doLS)   #Return回车事件  Enter 鼠标移动事件
        self.dirn.pack(fill=X, expand=True)

        self.bfm = Frame(self.top)
        self.clr = Button(self.bfm, text='Clear', command=self.clrDir, activeforeground='white', activebackground='blue')
        self.ls = Button(self.bfm, text='List Directory', command=self.doLS, activeforeground='white', activebackground='green')
        self.quit = Button(self.bfm, text='Quit', command=self.top.quit, activeforeground='white', activebackground='red')
        self.clr.pack(side=LEFT)
        self.ls.pack(side=LEFT)
        self.quit.pack(side=LEFT)
        self.bfm.pack()

        if initdir: #初始化GUI，程序从当前目录开始工作
            self.cwd.set(os.curdir)
            self.doLS()

    def clrDir(self, ev=None):
        self.cwd.set('')

    def setDirAndGo(self, ev=None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')    # config 重新配置
        check = self.dirs.get(self.dirs.curselection()) # curselection() 返回当前选中项的索引  get() 根据索引获取列表中索引的值
        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.doLS()

    def doLS(self, ev=None):
        error = ''
        tdir = self.cwd.get()
        if not tdir:
            tdir = os.curdir

        if not os.path.exists(tdir):
            error = tdir+':no such file'
        elif not os.path.isdir(tdir):
            error = tdir+':not a directory'

        if error:
            self.cwd.set(error)
            self.top.update()
            sleep(2)
            if not (hasattr(self, 'last') and self.last):
                self.last = os.curdir
            self.cwd.set(self.last)
            self.dirs.config(selectbackground='LightSkyBlue')
            self.top.update()
            return
        
        self.cwd.set('FETCHING DIRECTORY CONTENTS...')
        self.top.update()
        dirlist = os.listdir(tdir)
        dirlist.sort()
        os.chdir(tdir)
        self.dir1.config(text=os.getcwd())
        self.dirs.delete(0, END)
        self.dirs.insert(END, os.curdir)
        self.dirs.insert(END, os.pardir)
        for eachFile in dirlist:
            self.dirs.insert(END, eachFile.decode('gbk'))
        self.cwd.set(os.curdir)
        self.dirs.config(selectbackground="LightSkyBlue")

def main():
    d = DirList(os.curdir)
    mainloop()

if __name__ == '__main__':
    main()





# -*- coding:utf-8 -*-

'''
目录遍历程序
从当前目录开始并提供文件列表功能。双击列表中的任意其他目录都会让改工具转向这个心的目录，
同时用新的目录中的文件列表替换原来的文件列表
'''
'''
StringVar https://blog.csdn.net/wuxiushu/article/details/52515926
'''