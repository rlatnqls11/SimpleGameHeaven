import pygame
import os
from tkinter import *

pygame.init()

window = Tk()
window.title("심플 게임천국(Simple GameHeaven)")
window.geometry('710x400')
window.resizable(width=False, height=False)

photo = PhotoImage(file = "images/bg.png")
bglabel = Label(window, image = photo)
bglabel.pack()

def windowquit():
    mySound.stop()
    window.destroy()

def soundstop():
    mySound.stop()
    Sob['text'] = "노래 켜기"
    Sob['command'] = soundstart

def soundstart():
    mySound.play(-1)
    Sob['text'] = "노래 끄기"
    Sob['command'] = soundstop

def gamehelp():
    newwindow5 = Toplevel()
    newwindow5.geometry('500x630')
    newwindow5.resizable(width=False, height=False)
    newwindow5.title("게임 설정")
 
    photo3 = PhotoImage(file = "images/bg3.png")
    
    labels = Label(newwindow5, image = photo3)
    labels.pack()

    newwindow5.mainloop()
    
    
Sb = Button(window, text = "게임 시작", fg = "white", bg = "black", width =10, height=2)
Sb.pack()
Sb.place(x=340,y=150)

Sb2 = Button(window, text = "게임 시작", fg = "white", bg = "black", width =10, height=2)
Sb2.pack()
Sb2.place(x=340,y=150)

Hb = Button(window, text = "게임 설정", fg = "white", bg = "green", command = gamehelp, width =10, height=2)
Hb.pack()
Hb.place(x=340,y=210)

Eb = Button(window, text = "게임 나가기" ,fg = "white", bg = "red", command = windowquit, width =10, height=2)
Eb.pack()
Eb.place(x=340,y=270)

Sob = Button(window, text = "노래 켜기", command = soundstop ,fg = "white", bg = "pink", width =8, height=1)
Sob.pack()
Sob.place(x=0,y=0)

window.protocol('WM_DELETE_WINDOW', window)

mySound = pygame.mixer.Sound('music/basic.mp3')
mySound.set_volume(0.1)
mySound.play(-1)

window.mainloop()
