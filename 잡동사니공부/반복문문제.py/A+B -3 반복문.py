# #두 정수 A와 B를 입력받은 다음,A+B를 출력하는 프로그램 작성.
# 예제
# 5
# 1 1
# 2 3 
# 3 4   출력 2 5 7 17 7 
n = int(input())                       # n을 int 형태로 입력받는다
lst =[]                                # []를 이용하여 list 변수 지정

for i in range(n):                     # n번만큼 반복
    a, b = map(int, input().split())   # a, b 를 int 형태로 입력받는다(띄어쓰기로 구분)
    lst.append(a+b)                    # lst 리스트 변수에 a+b 값을 추가한다

for i in range(n):                     # n번만큼 반복(i에 0, 1, 2, ~ n-1 까지 순차입력)
    print(lst[i])                      # 리스트의 i번쨰 자료를 출력
