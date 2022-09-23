import pyautogui
import time
from tkinter import*  # 티킨터 사용
import os
from datetime import datetime, timedelta


def macro():
    time.sleep(1)
    pyautogui.click(x=1858, y=932)
    pyautogui.click(x=1858, y=932)
    time.sleep(5)
    pyautogui.click(x=1002, y=563)
    pyautogui.write('a6020933', 0.1)
    time.sleep(1)
    pyautogui.click(x=1010, y=590)
    pyautogui.write('09330933', 0.1)
    time.sleep(1)
    pyautogui.click(x=1082, y=574)
    time.sleep(1)
    pyautogui.click(x=1856, y=843)
    pyautogui.click(x=1856, y=843)


def refund():

    print("환불 요청 날짜")
    date = datetime.strptime(str(input()), "%Y%m%d")
    print("만료 날짜")
    date2 = datetime.strptime(str(input()), "%Y%m%d")
    # date2 = date + timedelta(days=int(input()))
    # print(date2)

    date3 = days = (date2 - date)
    a = (date3.days)

    print("결제 금액, 이용 일수")
    b, c = map(int, input().split())
    # b = 125000
    # c = 90

    d = (round(b/c)*a)
    f = b*0.1
    print("환불 받으실 금액은 {}원 입니다.".format(d-f))

    input()

    # 환불요청 날짜20220101 , 만료일자 20220130, 결제 금액 b , 이용 기간c
    import turtle as myTurtle

    n = 64

    myTurtle.shape('turtle')

    myTurtle.mainloop()


root = Tk()
root.title("시흥시 종합복지관")
# root.geometry("640x480") #가로
root.geometry("640x480+600+300")  # 플러스는 x,y좌표

# root.resizable(0,0) #x,y 변경 폴스값. 트루는 1 , 창크기 조절 가능여부
btn = Button(root, text="오픈", command=macro)
btn.pack()
btn2 = Button(root, text="환불 계산기", command=refund)
btn2.pack()
root.mainloop()  # 창이 닫히지 않게?하는 코드.20933
