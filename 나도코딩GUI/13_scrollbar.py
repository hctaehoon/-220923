from logging import warning
import tkinter.messagebox as msbox # as = 이름변경시 유용
from tkinter import*
from typing import List



root =Tk()
root.title("시흥시 종합복지관")
root.geometry("640x480+600+300")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right",fill="y")


listbox = Listbox(frame, selectmode="extended",height=10,yscrollcommand=scrollbar.set)
for i in range(1,32):
  listbox.insert(END,str(i)+"일")
  
listbox.pack()

scrollbar.config(command=listbox.yview) #내릴 때 동작하게 함.
















root.mainloop()