import pygame
import os
from tkinter import *

# pygame 초기화
pygame.init()

# window 창 생성
window = Tk()
window.title("심플 게임천국(Simple GameHeaven)")
window.geometry('710x400')

# 전체화면 비활성화
window.resizable(width=False, height=False)

# 이미지 삽입
photo = PhotoImage(file = "images/bg.png")
bglabel = Label(window, image = photo)
bglabel.pack()

# 음악 변수
v_size = 0.1

def maingame():
    def OnePbutton():
        newwindow2.title("-1인용 게임-")
        
        #Fb의 텍스트를 "2인용 게임보기"로 변경
        Fb['text'] = "2인용 게임보기"
        
        #Fb의 커맨드를 TwoPbutton으로 변경
        Fb['command'] = TwoPbutton
        
        Gb1['text'] = "퀴즈맞추기"
        Gb1['command'] = quizgame
        
        #Gb1의 이미지를 photo4로 변경
        Gb1['image'] = photo4
        
        Gb2['text'] = "재수강 피하기"
        Gb2['command'] = avoidgame
        Gb2['image'] = photo5
  
    def TwoPbutton():
        newwindow2.title("-2인용 게임-")
        Fb['text']= "1인용 게임보기"
        Fb['command'] = OnePbutton
        
        Gb1['text'] = "오목"
        Gb1['command'] = omokgame
        Gb1['image'] = photo6
        
        Gb2['text'] = "체스"
        Gb2['command'] = chessgame
        Gb2['image'] = photo7

    def quizgame():
        newwindow8 = Toplevel()
        newwindow8.geometry('300x100')
        newwindow8.resizable(width=False, height=False)
        newwindow8.title("<퀴즈 맞추기>")
        newwindow8.configure(bg='Steel blue')
        newwindow8.protocol('WM_DELETE_WINDOW', newwindow8)

        def game1():
            # Quizgame.py 실행
            os.system("Quizgame.py")

        def help2():
            newwindow9 = Toplevel()
            newwindow9.geometry('360x90')
            newwindow9.resizable(width=False, height=False)
            newwindow9.title("<퀴즈 맞추기>")
            newwindow9.configure(bg='white')

            label01 = Label(newwindow9, text = "-게임 설명-\n이 게임은 퀴즈를 맞추는 게임으로 총 10개의 퀴즈가 존재합니다.\n게임 안에 퀴즈의 정답에 대한 힌트와 도움말이 별도로 존재합니다.\n\n-조작법-\n마우스 좌클릭 및 엔터키 사용",font = ("Candara",9,"bold"))
            label01.pack()

            
        Sgb = Button(newwindow8, text = "플레이", command = game1, fg = "white", bg = "black", width =10, height=2)
        Sgb.pack()
        Sgb.place(x=10,y=30)

        Hgb = Button(newwindow8, text = "도움말", command = help2, fg = "white", bg = "green", width =10, height=2)
        Hgb.pack()
        Hgb.place(x=110,y=30)

        Egb = Button(newwindow8, text = "뒤로가기" , command = newwindow8.destroy ,fg = "white", bg = "red", width =10, height=2)
        Egb.pack()
        Egb.place(x=210,y=30)

    def avoidgame():
        newwindow10 = Toplevel()
        newwindow10.geometry('300x100')
        newwindow10.resizable(width=False, height=False)
        newwindow10.title("<재수강 피하기>")
        newwindow10.configure(bg='Steel blue')
        newwindow10.protocol('WM_DELETE_WINDOW', newwindow10)

        def game2():
            os.system('AvoidGame.py')

        def help3():
            newwindow11 = Toplevel()
            newwindow11.geometry('345x90')
            newwindow11.resizable(width=False, height=False)
            newwindow11.title("<재수강 피하기>")
            newwindow11.configure(bg='white')
            
            label02 = Label(newwindow11, text = "-게임 설명-\n이 게임은 하늘에서 떨어지는 F 학점을 피하는 게임으로\nF 학점을 부딪히면 죽고, 1초마다 피한 시간이 1씩 증가합니다.\n\n-조작법-\n방향키(←→↑↓) 사용",font = ("Candara",9,"bold"))
            label02.pack()

            
        Sgb = Button(newwindow10, text = "플레이", command = game2, fg = "white", bg = "black", width =10, height=2)
        Sgb.pack()
        Sgb.place(x=10,y=30)

        Hgb = Button(newwindow10, text = "도움말", command = help3, fg = "white", bg = "green", width =10, height=2)
        Hgb.pack()
        Hgb.place(x=110,y=30)

        Egb = Button(newwindow10, text = "뒤로가기" , command = newwindow10.destroy, fg = "white", bg = "red", width =10, height=2)
        Egb.pack()
        Egb.place(x=210,y=30)

    def omokgame():
        newwindow12 = Toplevel()
        newwindow12.geometry('300x100')
        newwindow12.resizable(width=False, height=False)
        newwindow12.title("<오목>")
        newwindow12.configure(bg='Steel blue')
        newwindow12.protocol('WM_DELETE_WINDOW', newwindow12)

        def game3():
            os.system('omok.py')

        def help4():
            newwindow13 = Toplevel()
            newwindow13.geometry('390x215')
            newwindow13.resizable(width=False, height=False)
            newwindow13.title("<오목>")
            newwindow13.configure(bg='white')
   
            label03 = Label(newwindow13, text = """-게임 설명-\n이 게임은 오목으로 흰돌 한번, 검은돌 한번씩 번갈아가며 돌을 놓습니다.\n 이때,같은 색깔의 돌을 다섯개 먼저 일렬로
세우는 사람이 승리합니다.(대각선도 포함)\n\n-조작법-\n왼쪽 마우스 클릭만 사용\n
-용어 설명-\nUndo = 한번 무르기\nUndo All = 전부 무르기\nRedo = 무르기 취소\nHide number = 숫자 숨기기\nNew Game = 새롭게 게임시작\nQuit Game = 나가기""",font = ("Candara",9,"bold"))
            label03.pack()

            
        Sgb = Button(newwindow12, text = "플레이", command = game3, fg = "white", bg = "black", width =10, height=2)
        Sgb.pack()
        Sgb.place(x=10,y=30)

        Hgb = Button(newwindow12, text = "도움말", command = help4, fg = "white", bg = "green", width =10, height=2)
        Hgb.pack()
        Hgb.place(x=110,y=30)

        Egb = Button(newwindow12, text = "뒤로가기" , command = newwindow12.destroy, fg = "white", bg = "red", width =10, height=2)
        Egb.pack()
        Egb.place(x=210,y=30)

    def chessgame():
        newwindow14 = Toplevel()
        newwindow14.geometry('300x100')
        newwindow14.resizable(width=False, height=False)
        newwindow14.title("<체스>")
        newwindow14.configure(bg='Steel blue')
        newwindow14.protocol('WM_DELETE_WINDOW', newwindow14)

        def game4():
            os.system('ChessMain.py')

        def help5():
            newwindow15 = Toplevel()
            newwindow15.geometry('880x410')
            newwindow15.resizable(width=False, height=False)
            newwindow15.title("<체스>")
            newwindow15.configure(bg='white')
            
            label04 = Label(newwindow15, text = """-게임 설명-\n이 게임은 체스로 흰말 한번, 검은말 한번씩 번갈아가며 말을 한번씩 움직입니다.(실행을 위해선 넘파이를 필수로 설치해야함)\n 이때, 각 진영의 가운데에 있는 킹을 먼저 먹은 사람이 승리합니다.
\n-말 설명-\n폰 : 가장 기본적인 말로 각 진영마다 8개씩 존재합니다\n 이들은 게임을 맨 처음 시작할때 2번재 줄과 7번째 줄에 존재하며\n맨 처음에는 2칸 또는 1칸을 앞으로만 움직일 수 있고, 한번 움직이고 나면 무조건 1칸씩 앞으로만 움직일 수 있습니다.
\n 단, 적이나 아군의 말을 넘을 수는 없습니다. 공격은 대각선 1칸으로만 1번 가능합니다.\n\n룩  : 각 진영마다 모서리에  2개씩 존재합니다.
\n 이들은 상,하,좌,우로 원하는 칸수만큼 움직일 수 있습니다. 단, 적이나 아군의 말을 넘을 수는 없습니다.
\n나이트 : 각 진영마다 룩의 오른쪽과 왼쪽에 1개씩 존재합니다.\n이들은 상,하,좌,우 중에서 원하는 칸으로 2칸 움직인 후 좌,우로 움직였을 경우 상 또는 하로 1칸\n상,하로 움직였을 경우 좌,우로 한칸 움직일 수 있습니다. 이들은 적이나 아군의 말을 넘을 수 있습니다.
\n비솝 : 각 진영마다 나이트의 오른쪽과 왼쪽에 1개씩 존재합니다.\n이들은 오직 대각선으로만 원하는 방향으로 원하는칸수만큼 움직일 수 있습니다. 단, 적이나 아군의 말을 넘을 수는 없습니다.
\n킹 : 체스에서 가장 중요한 왕으로, 오른쪽에서 4번째 칸에 존재합니다.\n이는 상,하,좌,우,대각선으로 1칸씩만 움직일 수 있습니다. 킹으로 다른 말을 잡을 수는 있지만, 킹으로 킹은 잡을 수 없습니다. 킹이 잡히면 게임은 패배하게 됩니다.
\n퀸 : 킹의 왼쪽에 존재합니다. 체스에서 가장 강력한 말로, 상,하,좌,우,대각선 어느 방향이든 원하는 만큼 이동이 가능합니다. 단, 적이나 아군의 말을 넘을 수는 없습니다.
\n-조작법-\n왼쪽 마우스 클릭만 사용, 흰색 말이 무조건 선공""",font = ("Candara",9,"bold"))
            label04.pack()


        Sgb = Button(newwindow14, text = "플레이", command = game4, fg = "white", bg = "black", width =10, height=2)
        Sgb.pack()
        Sgb.place(x=10,y=30)

        Hgb = Button(newwindow14, text = "도움말", command = help5, fg = "white", bg = "green", width =10, height=2)
        Hgb.pack()
        Hgb.place(x=110,y=30)

        Egb = Button(newwindow14, text = "뒤로가기" , command = newwindow14.destroy, fg = "white", bg = "red", width =10, height=2)
        Egb.pack()
        Egb.place(x=210,y=30)
        
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

    Gb1 = Button(newwindow2, text = "퀴즈 맞추기",command = quizgame, borderwidth=0 , image=photo4)
    Gb1.pack()
    Gb1.place(x=100,y=200)

    photo5 = PhotoImage(file="images/button3.png")

    Gb2 = Button(newwindow2, text = "재수강 피하기",command = avoidgame, borderwidth=0, image=photo5)
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
    #노래 멈춤
    mySound.stop()

    #윈도우 창 꺼짐
    window.destroy()

def gamehelp():
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
            
            # 입력받은 값 출력
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

    def soundstop():
        mySound.stop()
        Sb['text'] = "노래 켜기"
        Sb['command'] = soundstart

    def soundstart():
        mySound.play(-1)
        Sb['text'] = "노래 끄기"
        Sb['command'] = soundstop

    def soundup():
        global v_size
        mySound.set_volume(v_size)
        v_size += 0.02

    def sounddown():
        global v_size
        mySound.set_volume(v_size)
        v_size -= 0.02
        
    newwindow5 = Toplevel()
    newwindow5.geometry('500x630')
    newwindow5.resizable(width=False, height=False)
    newwindow5.title("게임 설정")
 
    photo3 = PhotoImage(file = "images/bg3.png")
    
    labels = Label(newwindow5, image = photo3)
    labels.pack()

    Pdb = Button(newwindow5, text = "제작자\n정보", command = producer, bg = "Steel Blue", font = ("Arial",9,"bold"))
    Pdb.pack()
    Pdb.place(x=185,y=180)

    Sb = Button(newwindow5, text = "노래 끄기", command = soundstop, bg = "Navajo White", font = ("Arial",9,"bold"))
    Sb.pack()
    Sb.place(x=170,y=38)

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

# 윈도우 x버튼 비활성화
window.protocol('WM_DELETE_WINDOW', window)

mySound = pygame.mixer.Sound('music/basic.mp3')
mySound.set_volume(v_size)
mySound.play(-1)

window.mainloop()
