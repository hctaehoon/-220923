# setType1 ={}
# b =42
# for i in range(10):
#   c = int(input())
#   a=c%b
# print(a)
# print(len(setType1))

arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr)
print(len(arr))