# Simple game in python

import tkinter as tk

from tkinter import messagebox
 
question = [
		#1번 문제
		("① 소프트웨어 지적재산권에는 '저작권', '특허권', '상표권' '0000'이 있다 빈칸에 들어갈 말은 무엇인가?","영업비밀"),
		#2번 문제
		("② 저작권과는 달리 일정한 방식으로 출원해야 하며, 심사를 통과한 후 등록되어야만 권리가 발생하는 소프트웨어 지적재산권은 무엇인가?", "특허권"),
		#3번 문제
		("③ 독점적인 의미의 저작권(copyright)과 반대되는 개념으로 저작권을 기반으로 한 정보의 공유를 위한 조치하는 말은 무엇인가?", "copyleft"),
                #4번 문제
                ("④ 메사추세츠 공과대학교(MIT)를 기원으로 하는 소프트웨어 라이선스 이고 여러 라이선스 중에서 매우 제한이 느슨하며 BSD계열 라이선스의 이름은 무엇인가?","MIT라이선스" ),
                #5번 문제
                ("⑤ 2005년 리눅스 개발자인 리누즈 토발즈가 개발하였고 GitHub웹 사이트가 존재, 대중성과 안정성때문에 많은 기업에서 버전 관리 시스템으로 채택한 분산 버전 관리 시스템은 무엇인가?","Git"),
                #6번 문제
		("⑥ Git의 장점으로 모든 작업이 '00'에서 이루어지고 네트워크 사용은 '00'저장소로 저장할때 한 번 이루어지므로 개발 시 처리속도가 빠르다. 빈칸에 들아갈 말은 모두  무엇인가?","로컬, 원격" ),
		#7번 문제
		("⑦ Git에서 저장소에 브랜치를 추가하여 '이름'의 브랜치를 만드는 명령어는 무엇인가?","git branch 이름"),
		#8번 문제
		("⑧ 커밋 내역을 확인하는 기능인 git log 에서 브랜치 분가와 병합 내역을 아스키 그래프로 보여주는 명령어인 git log --'00000'은 무엇인가?","graph"),
                #9번 문제
                ("⑨ git revert 명령은 이전 커밋을 남겨두는 명령어지만 git '00000'은  이전 커밋을 남기지 않고 새로운 커밋을 남기는 명령어는 무엇인가?","reset"),
                #10번 문제
                ("⑩ git reset 명령은 hard 모드가 아니라면 저장소 디렉토리의 파일 내용은 명령을 실행한 시점 그대로 남는다 'O/X'","O")
 
]
#리스트의 길이(10)
numdom = len(question)

#점수
score = 0

#문제 갯수
totalQuestions = 0

def d1():
        #전역 변수 totalQuestions, score, entry 사용
	global totalQuestions, score, entry
	if totalQuestions == numdom:

            #텍스트 박스 숨김    
	    text.pack_forget()
	    entry.pack_forget()
	    
	    #정답률 산출 공식
	    percent = score / totalQuestions * 100

	    #버튼에 텍스트 삽입
	    button['text'] = f"정답률: {percent}%\n 점수:{score}점\n 합격여부를 확인할려면 클릭하세요"

            #버튼을 클릭시 gameover 문단 실행
	    button['command'] = gameover

	    #버튼 위치
	    button.pack()
	    return

	#totalQuestions과 0을 비교
	if totalQuestions == 0:
	    answer()

	#텍스트박스 크기	
	text['height'] = 7
	text['width'] = 80

	#텍스트박스 배경색깔
	text['bg'] = 'white'

	#텍스트박스 삭제 범위 지정
	text.delete("1.0",tk.END)

	#텍스트박스 삽입 범위
	text.insert("1.0",question[totalQuestions][0])

	#버튼 숨김
	button.pack_forget()
	
	totalQuestions+=1

def gameover():
	global score
	if score >=7:
	    print("당신은 합격입니다! 오픈소스 소프트웨어 강의를 열심히 들으셨군요!!")
	else:
	    print("당신은 불합격입니다. 강의를 열심히 들으세요!!")
 
def answer():
	global entry
	
	#텍스트박스 속성
	entry = tk.Entry(window, textvariable=ans, bg="yellow", font="Arial 20")
	entry.pack()
	
	#이벤트 작동시 실행할 함수 설정(Return = 엔터키 입력)
	entry.bind("<Return>", lambda x: check())
	entry.focus()

def empty_textbox():
		ans.set("")
		d1()

def check():
	global n, score
	text.delete("1.0",tk.END)

	#입력받는 값의 범위 비교
	if ans.get() == question[totalQuestions-1][1]:
                
                #정답일 시 텍스트박스 색 및 글자 전환
		text.insert(tk.END, "정답입니다! :) ")

		#정답일 시 점수 추가
		score+=1
		text['bg'] = "green"
	else:
                #오답일 시 텍스트박스 색 및 글자 전환
		text.insert(tk.END, "오답입니다 :( ")
		text['bg'] = "red"
	text.after(1000, empty_textbox)

def clickButton() :
        messagebox.showinfo("도움말","게임시작을 누른 후, 빈칸에 답을 적고 엔터를 눌러!\n혹시 퀴즈가 어렵다면 오른쪽의 캐릭터를 눌러봐!")

def duduButton() :
        messagebox.showinfo("정답","1. 영업비밀\n2. 특허권\n3. copyleft\n4. MIT라이선스\n5. Git\n6. 로컬, 원격\n7. git branch 이름\n8. graph\n9. reset\n10. O ")
                                           
 
window = tk.Tk()
window.title("오픈소스 소프트웨어  Quiz!!!")
window.geometry("1000x500")

window.resizable(width=False, height=False)
        
#하늘색 RGB 코드
window['bg'] = '#FFDCDC'

#두두 그림 삽입
image = tk.PhotoImage(file="images/ch.png")
image_button = tk.Button(window, image = image, command=duduButton)
image_button.pack()
image_button.place(x=780, y=300)

label = tk.Label(window, text = "GitHub Quiz", bg="green", font="Arial 48")
label.pack()

rules = """이 게임은 오픈소스 소프트웨어 관련 퀴즈입니다. 오픈소스 소프트웨어를 공부하기 위해 제작되었습니다.

"""
text = tk.Text(window, bg="white",height=7,font="Arial 20")
text.insert("1.0", rules)
text.pack()

b1 = tk.Button(window, text="(도움말)", bg="white", fg="red", command=clickButton, font="Arial 10")
b1.place(x=0, y=472)
b1.pack

button = tk.Button(window, text="게임시작", bg="black", fg="white", command=d1, font="Arial 20")
button.pack()

ans = tk.StringVar()

window.mainloop()


