from logging import warning
import tkinter.messagebox as msbox # as = 이름변경시 유용
from tkinter import*
from typing import List



root =Tk()
root.title("시흥시 종합복지관")
root.geometry("640x480+600+300")





# btn1 = Button(root,text="버튼1")
# btn2 = Button(root,text="버튼2")

# # btn1.pack(side="left")
# # btn2.pack(side="left")
# btn1.grid(row=0,column=0)  #그리드 . 좌표로 0,0
# btn2.grid(row=1,column=1)  #그리드 . 좌표로 0,0


#맨 윗줄
btn_f16 = Button(root, text="F16")
btn_f17 = Button(root, text="F17")
btn_f18 = Button(root, text="F18")
btn_f19 = Button(root, text="F19")

btn_f16.grid(row=0, column=0)
btn_f17.grid(row=0, column=1)
btn_f18.grid(row=0, column=2)
btn_f19.grid(row=0, column=3)

#clear 줄

btn_clear = Button(root, text="clear")
btn_equal = Button(root, text="=")
btn_div = Button(root, text="/")
btn_mul = Button(root, text="*")

btn_clear.grid(row=1, column=0)
btn_equal.grid(row=1, column=1) 
btn_div.grid(row=1, column=2) 
btn_mul.grid(row=1, column=3)

# 7시작 줄 

btn_7 = Button(root, text="7")
btn_8 = Button(root, text="8")
btn_9 = Button(root, text="9")
btn_sub = Button(root, text="sub")

btn_7 .grid(row=2, column=0)
btn_8.grid(row=2, column=1) 
btn_9.grid(row=2, column=2) 
btn_sub.grid(row=2, column=3)









root.mainloop()