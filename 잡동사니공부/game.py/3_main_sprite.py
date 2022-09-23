# import pygame


from numpy import character
import pygame


pygame.init() #초기화. 반드시필요

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
# 480 * 640 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Tae Hun game")


#배경 이미지 불러오기 
background = pygame.image.load("C:\\\\Users\\\\user\\\\Desktop\\\\a602093309330933\\\\pythonWorkspace\\\\game.py\\\\background.png")

#스프라이트 불러오기(캐릭터)

character =pygame.image.load("C:\\Users\\user\\Desktop\\a602093309330933\\pythonWorkspace\\game.py\\character.png")
character_size = character.get_rect().size #이미지 크기 구해봄
character_width = character_size[0] #캐릭터 가로
character_height = character_size[1] #캐릭터 세로
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로의 절반 크기
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아래에.
#이벤트 루프 실행
running = True #게임이 진행중인가?
while running:
  for event in pygame.event.get():  #외워야함. 이벤트 루프 # 이벤트가 발생하였는가?
    if event.type == pygame.QUIT:   #창이 닫히는 이벤트가 발생하였는가?
      running = False #게임이 진행중이 아님
      
      
    
  
  screen.blit(background, (0, 0))
  screen.blit(character, (character_x_pos,character_y_pos))
  
  pygame.display.update()

    
   


#running 이 False 가 된다면 
pygame.quit()

#배경 넣기