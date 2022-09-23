N = int(input())
b = []
a = list(map(int,input().split()))
c = max(a) 
for i in a:
  b.append(i/c*100)
print(sum(b)/N)

  
 
