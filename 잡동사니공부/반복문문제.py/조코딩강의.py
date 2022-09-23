# # # # 조건문 if
# # # # True False로 나뉨

# # # # money = 5000
# # # # if money > 0:
# # # #   print("택시 타고가")
# # # # else:
# # # #   print("돈없어 걸어가")

# # # # 반복문
# # # # 나무를 10번 찍는다
# # # treehit=0
# # # while treehit < 10:
# # #   treehit = treehit +1
# # #   print("나무를 %d번 찍었습니다."% treehit)
# # #   if treehit == 10:
# # #     print("나무 넘어갑니다.")
# # coffee = 10
# # money = 300
# # while money:
# #   print("돈을 받았음 커피 드림")
# #   coffee = coffee - 1
# #   money = money - 100
# #   if not coffee:
# #     print("커피 끝")
# #   elif not money:
# #     print("돈 없어서 끝")
# #     break

# # a= 0
# # while a < 10:
# #   a= a+1
# #   if a % 2 == 0:
# #     continue
# # #   print(a)
# # while True: #무한 루프
# #   print("안녕하세요")

# # for 변수 in 리스트(또는 튜플,문자열):
# # #   수행 문장1 2 . . .

# # test_list = ['one','two','three']
# # # for i in test_list:
# # #   print(i)
# # a = [(1,2),(3,4,),(5,6)]
# # for (first, last) in a:
# #   print(first + last)

# marks = [90,25,67,45,80]
# number = 0
# for mark in marks:
#   number = number + 1
#   if mark < 60:
#     continue
#   print("%d번 학생은 합격입니다.축하합니다." % number)


# sum = 0
# for i in range(1,11):
#   print(i)
#   sum = sum + i
# print(sum)
# for i in range(2,10):
#   for j in range(1,10):
#     print(i*j, end= " ")
#   print(" ")
# 리스트 내포?


result = [x*y for x in range(2, 10) for y in range(1, 10)]
result = tuple(result)
print(result , end= " ")
