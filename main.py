import pygame
import os
from tkinter import *

window = Tk()
window.title("심플 게임천국(Simple GameHeaven)")
window.geometry('710x400')
window.resizable(width=False, height=False)
    
Sb = Button(window, text = "게임 시작", fg = "white", bg = "black", width =10, height=2)
Sb.pack()
Sb.place(x=340,y=150)

Sb2 = Button(window, text = "게임 시작", fg = "white", bg = "black", width =10, height=2)
Sb2.pack()
Sb2.place(x=340,y=150)

Hb = Button(window, text = "게임 설정", fg = "white", bg = "green", width =10, height=2)
Hb.pack()
Hb.place(x=340,y=210)

Eb = Button(window, text = "게임 나가기" ,fg = "white", bg = "red", width =10, height=2)
Eb.pack()
Eb.place(x=340,y=270)

window.protocol('WM_DELETE_WINDOW', window)

window.mainloop()