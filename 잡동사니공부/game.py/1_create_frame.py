# import pygame


import pygame


pygame.init() #초기화. 반드시필요

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
# 480 * 640 크기
screen= pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Tae Hun game")

#이벤트 루프 실행
running = True #게임이 진행중인가?
while running:
  for event in pygame.event.get():  #외워야함. 이벤트 루프 # 이벤트가 발생하였는가?
    if event.type == pygame.QUIT:   #창이 닫히는 이벤트가 발생하였는가?
      running = False #게임이 진행중이 아님

#running 이 False 가 된다면 
pygame.quit()

#배경 넣기