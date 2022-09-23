#N개의 정수가 주어진다. 이때, 최솟값과 최대값을 구해

N=int(input()) #N 입력값.
# lst= list(map(int,input().split())) #리스트를 바로 만들어 5개의 정수입력
# lst.sort() #오름차순
# print(min(lst), max(lst)) #최소, 최댓값.

#내풀이문제. N을 충족하지 않음.
#밑엔 다른 풀이들.
#print(min(lst),max(lst)) 최소, 최대 출력 
#N을 사용하는 코드

for i in range(N):
  a= list(map(int,input()))
  
print(min(a),max(a))


