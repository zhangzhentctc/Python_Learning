#-*- coding: UTF-8 -*-
__author__ = '007'
__date__ = '2016/4/7'

from tkinter import *
root = Tk() # 初始化Tk()
root.title("scrl-test")    # 设置窗口标题
root.geometry()    # 设置窗口大小 注意：是x 不是*
def print_item(event):
    print( lb.get(lb.curselection()))
var = StringVar()
lb = Listbox(root, height=5, selectmode=BROWSE, listvariable = var)
lb.bind('<ButtonRelease-1>',print_item)
list_item = [1,2,3,4,5,6,7,8,9,0]
for item in list_item:
    lb.insert(END,item)
scrl = Scrollbar(root)
scrl.pack(side=RIGHT,fill=Y)
lb.configure(yscrollcommand=scrl.set)   # 指定Listbox的yscrollbar的回调函数为Scrollbar的set，表示滚动条在窗口变化时实时更新
lb.pack(side=LEFT,fill=BOTH)
scrl['command'] = lb.yview  # 指定Scrollbar的command的回调函数是Listbar的yview
root.mainloop()