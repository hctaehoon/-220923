import os 
from datetime import datetime, timedelta
print("환불 요청 날짜")
date = datetime.strptime(str(input()), "%Y%m%d")
print("만료 날짜")
date2 = datetime.strptime(str(input()), "%Y%m%d")
# date2 = date + timedelta(days=int(input()))
# print(date2)

date3= days=(date2 - date)
a=(date3.days)

print("결제 금액, 이용 일수")
b,c = map(int,input().split())
# b = 125000
# c = 90

d=(round(b/c)*a)
f= b*0.1
print("환불 받으실 금액은 {}원 입니다.".format(d-f))

input()

#환불요청 날짜20220101 , 만료일자 20220130, 결제 금액 b , 이용 기간c
import turtle as myTurtle

n = 64

myTurtle.shape('turtle')


myTurtle.mainloop()