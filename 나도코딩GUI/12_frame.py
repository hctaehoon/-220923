from logging import warning
import tkinter.messagebox as msbox # as = 이름변경시 유용
from tkinter import*



root =Tk()
root.title("시흥시 종합복지관")
root.geometry("640x480+600+300")

Label(root, text="메뉴 선택").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")
#메뉴


frame_burger = Frame(root, relief="solid",bd=1) #bd = 외곽선
frame_burger.pack(side="left",fill="both",expand=True)

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()
Button(frame_burger, text="데리버거").pack()
#음료
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right",fill="both",expand=True)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()
root.mainloop()