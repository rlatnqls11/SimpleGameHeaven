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

v_size = 0.1

def maingame():
    def OnePbutton():
        newwindow2.title("-1인용 게임-")
        Fb['text'] = "2인용 게임보기"
        Fb['command'] = TwoPbutton

        Gb1['text'] = "퀴즈맞추기"
        Gb1['image'] = photo4
        
        Gb2['text'] = "재수강 피하기"
        Gb2['image'] = photo5
  
    def TwoPbutton():
        newwindow2.title("-2인용 게임-")
        Fb['text']= "1인용 게임보기"
        Fb['command'] = OnePbutton
        
        Gb1['text'] = "오목"
        Gb1['image'] = photo6
        
        Gb2['text'] = "체스"
        Gb2['image'] = photo7
        
    photo2 = PhotoImage(file = "images/bg2.png")

    newwindow2 = Toplevel()
    newwindow2.geometry('710x400')
    newwindow2.resizable(width=False, height=False)
    newwindow2.title("-1인용 게임-")

    bg2label = Label(newwindow2, image = photo2);
    bg2label.pack()

    Bb = Button(newwindow2, text = "←", command = newwindow2.destroy, bg = "yellow")
    Bb.pack()
    Bb.place(x=0,y=0)

    photo4 = PhotoImage(file="images/button2.png")

    Gb1 = Button(newwindow2, text = "퀴즈 맞추기",borderwidth=0 , image=photo4)
    Gb1.pack()
    Gb1.place(x=100,y=200)

    photo5 = PhotoImage(file="images/button3.png")

    Gb2 = Button(newwindow2, text = "재수강 피하기", borderwidth=0, image=photo5)
    Gb2.pack()
    Gb2.place(x=400,y=200)

    Bb = Button(newwindow2, text = "←", command = newwindow2.destroy, bg = "yellow")
    Bb.pack()
    Bb.place(x=0,y=0)

    Fb = Button(newwindow2, text = "2인용 게임보기", command = TwoPbutton, bg = "Medium Sea Green")
    Fb.pack()
    Fb.place(x=310,y=0)

    photo6 = PhotoImage(file="images/button4.png")
    photo7 = PhotoImage(file="images/button5.png")

    newwindow2.protocol('WM_DELETE_WINDOW', newwindow2)
    newwindow2.mainloop()
    
def windowquit():
    mySound.stop()
    window.destroy()

def gamehelp():
    def producer():
        newwindow3 = Toplevel()
        newwindow3.geometry('250x70')
        newwindow3.title("제작자")

        newwindow3.protocol('WM_DELETE_WINDOW', newwindow3)
        bg3label = Label(newwindow3, text = "대구대학교 정보통신대학\n컴퓨터정보공학부 컴퓨터공학전공\n 21727594 김수빈\n 21727756 김동현");
        bg3label.pack()

        Bb3 = Button(newwindow3, text = "←", command = newwindow3.destroy, bg = "yellow")
        Bb3.pack()
        Bb3.place(x=0,y=0)

    def Mcopyright():
        newwindow6 = Toplevel()
        newwindow6.geometry('500x80')
        newwindow6.resizable(width=False, height=False)
        newwindow6.title("출처")

        label5 = Label(newwindow6,text="""=====================================================
Mountain Trials by Joshua McLean | http://mrjoshuamclean.com
Music promoted by https://www.mewpot.com
CC BY-SA 4.0 | https://creativecommons.org/licenses/by-sa/4.0/
==================================================""")
        label5.pack()
    
        Bb3 = Button(newwindow6, text = "←", command = newwindow6.destroy, bg = "yellow")
        Bb3.pack()
        Bb3.place(x=0,y=0)

        newwindow6.protocol('WM_DELETE_WINDOW', newwindow6)
        newwindow6.mainloop()

    def soundup():
        global v_size
        mySound.set_volume(v_size)
        v_size += 0.02

    def sounddown():
        global v_size
        mySound.set_volume(v_size)
        v_size -= 0.02

    def soundstop():
        mySound.stop()
        Sb['text'] = "노래 켜기"
        Sb['command'] = soundstart

    def soundstart():
        mySound.play(-1)
        Sb['text'] = "노래 끄기"
        Sb['command'] = soundstop

    def nickname():
        newwindow4 = Toplevel()
        newwindow4.geometry('300x120')
        newwindow4.resizable(width=False, height=False)
        newwindow4.title("닉네임")
        newwindow4.configure(bg='Rosy Brown')

        e = Entry(newwindow4, width=30, borderwidth=10, fg="red", bg="yellow")
        e.pack()
        e.insert(0, "닉네임을 적어주세요")

        def click():
            hello = "당신의 닉네임 : " + str(e.get())[0:]
            label8 = Label(newwindow4, text=hello)
            label8.pack()

        Bb2 = Button(newwindow4, text = "←", command = newwindow4.destroy, bg = "yellow")
        Bb2.pack()
        Bb2.place(x=0,y=0)

        buttonz = Button(newwindow4, text="확인", command = lambda:[click(),error()])
        buttonz.pack()

        newwindow4.protocol('WM_DELETE_WINDOW', newwindow4)
        newwindow4.mainloop()
        
    newwindow5 = Toplevel()
    newwindow5.geometry('500x630')
    newwindow5.resizable(width=False, height=False)
    newwindow5.title("게임 설정")
 
    photo3 = PhotoImage(file = "images/bg3.png")
    
    labels = Label(newwindow5, image = photo3)
    labels.pack()

    Sb = Button(newwindow5, text = "노래 끄기", command = soundstop, bg = "Navajo White", font = ("Arial",9,"bold"))
    Sb.pack()
    Sb.place(x=170,y=38)

    Pdb = Button(newwindow5, text = "제작자\n정보", command = producer, bg = "Steel Blue", font = ("Arial",9,"bold"))
    Pdb.pack()
    Pdb.place(x=185,y=180)

    Vub = Button(newwindow5, text = "업", command = soundup, bg = "violet", font = ("Arial",9,"bold"))
    Vub.pack()
    Vub.place(x=175,y=96)

    Vdb = Button(newwindow5, text = "다운", command = sounddown, bg = "violet", font = ("Arial",9,"bold"))
    Vdb.pack()
    Vdb.place(x=175,y=128)

    Nb = Button(newwindow5, text = "닉네임\n설정", command = nickname, bg = "Light Cyan", font = ("Arial",9,"bold"))
    Nb.pack()
    Nb.place(x=185,y=255)

    Eb = Button(newwindow5, text = "노래 출처", command = Mcopyright ,fg = "black", bg = "papaya Whip", font = ("Arial",9,"bold"))
    Eb.pack()
    Eb.place(x=260,y=38)

    Bb = Button(newwindow5, text = "←", command = newwindow5.destroy, bg = "yellow")
    Bb.pack()
    Bb.place(x=0,y=0)

    newwindow5.protocol('WM_DELETE_WINDOW', newwindow5)
    newwindow5.mainloop()
    
def maingame2():
        newwindow7 = Toplevel()
        newwindow7.geometry('215x20')
        newwindow7.resizable(width=False, height=False)
        newwindow7.title("에러")
        
        Bb4 = Button(newwindow7, text = "←", command = newwindow7.destroy, bg = "yellow")
        Bb4.pack()
        Bb4.place(x=0,y=0)
        
        bg6label = Label(newwindow7, text = "게임 설정에서 닉네임을 설정해 주세요!", bg="Light Slate Gray",fg = "white");
        bg6label.pack()

        newwindow7.mainloop()

def error():
    Sb2.destroy()
        
Sb = Button(window, text = "게임 시작", fg = "white", command = maingame, bg = "black", width =10, height=2)
Sb.pack()
Sb.place(x=340,y=150)

Sb2 = Button(window, text = "게임 시작", fg = "white", command = maingame2, bg = "black", width =10, height=2)
Sb2.pack()
Sb2.place(x=340,y=150)

Hb = Button(window, text = "게임 설정", fg = "white", bg = "green", command = gamehelp, width =10, height=2)
Hb.pack()
Hb.place(x=340,y=210)

Eb = Button(window, text = "게임 나가기" ,fg = "white", bg = "red", command = windowquit, width =10, height=2)
Eb.pack()
Eb.place(x=340,y=270)

window.protocol('WM_DELETE_WINDOW', window)

mySound = pygame.mixer.Sound('music/basic.mp3')
mySound.set_volume(v_size)
mySound.play(-1)

window.mainloop()
