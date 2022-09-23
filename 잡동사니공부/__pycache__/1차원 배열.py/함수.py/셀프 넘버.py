# def selfnum():
#   numbers = set(range(1,10001))
#   remove = set()
#   for i in numbers:
#     for j in str(i):
#       i += int(j)
#     remove.add(i)
    
#   self = numbers - remove
#   for k in sorted(self):
#     print(k)
# selfnum()


numbers=set(range(1,10001))
remove = set()
for i in numbers:
  for j in str(i):
    i += int(j)
  remove.add(i)
  
self = numbers - remove
for k in sorted(self):
     print(k)
    
