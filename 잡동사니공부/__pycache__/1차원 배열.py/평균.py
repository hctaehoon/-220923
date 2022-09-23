N=int(input())
arr2=[]
sum=0
arr1 = list(map(int,input().split()))

# print(arr1)
# print(f)
for i in arr1:
  arr2.append(i/max(arr1)*100)
# print(sum(arr2)/len(arr2))
for i in arr2:
 sum += i
print(sum/N)



  

  