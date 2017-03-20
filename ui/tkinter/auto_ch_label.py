import tkinter
import random


def suijishu(a, b):
    text.delete(1.0, 'end')
    text.insert('end', random.randint(a, b))
    text.after(500, suijishu, a, b)


top = tkinter.Tk()
text = tkinter.Text(top)
text.pack(expand=1, fill='both')
suijishu(51, 100)

top.mainloop()