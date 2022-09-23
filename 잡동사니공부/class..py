class Unit:
 def __init__(self, name, hp ,speed):
   self.name = name
   self.hp = hp
   self.speed = speed
   print("{0}유닛이 생성되었습니다.".format(name))

 
 def move(self , location):
  print("[지상 유닛 이동]")
  print("{0} : {1} 방향으로 이동합니다.[속도 {2}]"\
  .format(self.name , location , self.speed))


 def damaged(self,damage):
 print("{0}:{1}데미지를 입었습니다.".format(self.name, damage))
 self.hp -= damage
 print("{0}:현재 체력은 {1}입니다.".format(self.name,damage))

class AttackUnit(Unit):
 def __init__(self,name,hp,speed,damage):
   Unit.__init__(self,name,hp,speed)
   self.damage = damage

 def Attack(self , location):
   print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
   .format(self.name, location , self.damage))

class Flyable:
 def __init__(self, flying_speed):
  self.flying_speed = flying_speed
 def fly(self,name,location):
  print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
  .format(name,location,self.flying_speed))
class FlyableAttackUnit(AttackUnit,Flyable):
 def __init__(self,name,hp,damage,flying_speed):
  AttackUnit. __init__(self,name,hp,0,damage)
  Flyable. __init__(self,flying_speed)
 def move(self,location):
  print("[공중 유닛 이동]")
  self.fly(self.name, location)


#벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐",80,10,20)

battleCruiser = FlyableAttackUnit("배틀크루져",500,25,3)

vulture.move("11시")
battleCruiser.move("9시")





