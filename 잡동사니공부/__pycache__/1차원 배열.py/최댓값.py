#9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을
# 찾고 그 최댓값이 몇 번째인가?


a =[]
for i in range(9):
  a.append(int(input()))
print(max(a))
print(a.index(max(a))+1)