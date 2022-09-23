import sys
# sys.stdin.readline
# sys.stdin.readline
T=int(sys.stdin.readline())
lst =[]
for i in range(T):
  a, b=map(int,sys.stdin.readline().split())
  lst.append(a+b)
sum=0 
for i in range(T):
  sum += 1
  print(f"Case #{sum}: {lst[i]}")
  
  #혼자 해결 완료.
  