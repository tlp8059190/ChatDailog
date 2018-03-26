#! /usr/bin/python
#-*- coding:UTF-8 -*-

#from PIL import Image
from Tkinter import *
import Tkinter as tk

window = tk.Tk()

#设置窗口名字和大小
window.title("with small teenager ")
window.geometry('500x380')

#设置透明窗口
window.attributes("-alpha", 0.97)

#创建几个Frame作为容器
f1 = tk.Frame(window, width = 350, height = 240, bg = 'grey')
f2 = tk.Frame(window, width = 350, height = 100, bg = 'white' )
f3 = tk.Frame(window, width = 150, height = 380)
f4 = tk.Frame(window, width = 66, height = 25, bg = 'pink')

#打开图片
#im = tk.PhotoImage(file = '1.png')
im = tk.PhotoImage(file = 'Seventh-Dwarf-85598.gif')

#创建几个元素
Text_left1 = Text(f1)
Text_left2 = Text(f2)
Label_right = Label(f3, imag = im)
Button_left3 = Button(f4, text = 'send', width = 8, bg = '#AFEEEE')

#使用grid设置每个容器的位置
f1.grid(row = 0, column = 0, padx = 3)
f2.grid(row = 1, column = 0, padx = 3, pady = 0)
f3.grid(row = 0, column = 1, rowspan = 3, padx = 2)
f4.grid(row = 2, column = 0, sticky = 'E', padx = 10)

#固定网格大小
f1.grid_propagate(0)
f2.grid_propagate(0)
f3.grid_propagate(0)
f4.grid_propagate(0)

#将元素填充到容器Frame中
Text_left1.grid()
Text_left2.grid()
Label_right.grid()
Button_left3.grid()

#主事件循环
window.mainloop()