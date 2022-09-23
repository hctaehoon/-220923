# class Calculator:
#   def __init__(self):
#     self.value= 0
    
#   def add(self,val):
#     self.value +=val
    
# class UpgradeCalculator(Calculator):
#   def minus(self,val):
#     self.value -=val
    
# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)

# print(cal.value)
# class Calculator:
#   def __init__(self):
#     self.value = 0
#   def add(self,val):
#     self.value += val
    
# class MaxLimitCalculator(Calculator):
#   def add(self,val):
#     if val >= 100:
#       return 100
    
      
# cal = MaxLimitCalculator()
# cal.add(50)
# cal.add(60)

# print(cal.value)

# print(all([1,2]))
# print(chr(ord('a'))=='a')
# print(abs(-3))
    


# print(list(filter(lambda x: x>0,[1,-3,2,0,-5,6])))

# print(hex(234)) oct 



# print(list(map(lambda a: a*3,[1,2,3,4])))

# print(max([-8,2,7,5,-3,5,0,1])+min([-8,2,7,5,-3,5,0,1]))
# a =[1,2,3]
# max([a])
# a =[]
# for i in range(9):
#   a.append(int(input()))

# print(max(a))
# print(a.index(max(a))+1)


# print(round(17/3,4))

# import sys
# print(sys.argv)
# import random
# a = []
# while True:
#   a.append((random.randint(1,46)))
#   if len(set(a)) == 5:
#     break
# print(a)
  