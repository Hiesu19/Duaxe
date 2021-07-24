import pygame
import random
from random import choice

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Đua xe')
clock = pygame.time.Clock()
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY=(89, 97, 93)
RED = (255,0,0)
GREEN = (0,255,0 )
YELLOW =(255, 238, 0)
ORANGE = (250, 144, 5)
PINK =(255, 0, 162)
BLUE =(00,0,255)
COL1=(245, 194, 66)
COL2=(37, 201, 204)
COL3=(87, 10, 242)
COL4=(128, 163, 59)
COL5=(128, 8, 44)
COL6=(255, 5, 47)
COL7=(51, 209, 27)
COL8=(61, 166, 115)
aray = [COL1,COL2,COL3,COL4,COL5,COL6,COL7,COL8]
background_x = 200
background_y = 0
background = pygame.image.load ('rd.png')

spend_up = 0.04
x_velocity = 1
y_velocity = 1
y_ray_do = 0
score = 0
#Khai biến xe
x_car = 380
y_car = 520
x_xe1=random.randint(200,250)
y_xe1=random.randint(-500,0)
x_xe2=random.randint(300,350)
y_xe2=random.randint(-500,0)
x_xe3=random.randint(400,450)
y_xe3=random.randint(-500,0)
x_xe4=random.randint(500,550)
y_xe4=random.randint(-500,0)
x_xe1a=random.randint(200,250)
y_xe1a=random.randint(-1060,-560)
x_xe2a=random.randint(300,350)
y_xe2a=random.randint(-1060,-560)
x_xe3a=random.randint(400,450)
y_xe3a=random.randint(-1060,-560)
x_xe4a=random.randint(500,550)
y_xe4a=random.randint(-1060,-560)

sfont1 = pygame.font.SysFont('consolas',30)
sfont2 = pygame.font.SysFont('consolas',20)
sfont3 = pygame.font.SysFont('consolas',80)
sfont4 = pygame.font.SysFont('consolas',40)
sfont5 = pygame.font.SysFont('consolas',20)
sfont6 = pygame.font.SysFont('consolas',33)
sfont7 = pygame.font.SysFont('consolas',10)
sfont8 = pygame.font.SysFont('consolas',28)
sound1=pygame.mixer.Sound('tick.wav')
sound2=pygame.mixer.Sound('bur.mp3')
ghi = False
nhan = False
running = True
start = False
stop = False
gameover = False
lock = False
lv = 1


while running:
	clock.tick(100)
	screen.fill(YELLOW)
	bien1_rect = pygame.draw.rect(screen , GRAY,(0,0,190,600))
	bien2_rect = pygame.draw.rect(screen , GRAY,(610,0,190,600))
	mouse_x,mouse_y= pygame.mouse.get_pos()
	
	background1_rect = screen.blit(background,(background_x,background_y))
	background2_rect = screen.blit(background,(background_x,background_y-600))
	if background_y - 600 >=0:
		background_y = 0
	if start:	
		background_y +=y_velocity
		y_ray_do+= y_velocity
		y_xe1 += y_velocity
		y_xe2 += y_velocity
		y_xe3 += y_velocity
		y_xe4 += y_velocity
		y_xe1a += y_velocity
		y_xe2a+= y_velocity
		y_xe3a += y_velocity
		y_xe4a += y_velocity

	if y_xe1 >600:
		x_xe1=random.randint(200,260)
		y_xe1=random.randint(-500,0)
		score+=lv
		y_velocity+=spend_up
		pygame.mixer.Sound.play(sound1)
	if y_xe2 >600:
		x_xe2=random.randint(300,360)
		y_xe2=random.randint(-500,0)
		score+=lv
		y_velocity+=spend_up
		pygame.mixer.Sound.play(sound1)
	if y_xe3 >600:
		x_xe3=random.randint(400,460)
		y_xe3=random.randint(-500,0)
		score+=lv
		y_velocity+=spend_up
		pygame.mixer.Sound.play(sound1)
	if y_xe4 >600:	
		x_xe4=random.randint(500,560)
		y_xe4=random.randint(-500,0)
		score+=lv
		y_velocity+=spend_up
		pygame.mixer.Sound.play(sound1)
	if y_xe1a >600:
		x_xe1a=random.randint(200,260)
		y_xe1a=random.randint(-1060,-460)
		score+=lv
		y_velocity+=spend_up
		pygame.mixer.Sound.play(sound1)
	if y_xe2a >600:
		x_xe2a=random.randint(300,360)
		y_xe2a=random.randint(-1060,-460)
		score+=lv
		y_velocity+=spend_up
		pygame.mixer.Sound.play(sound1)
	if y_xe3a >600:
		x_xe3a=random.randint(400,460)
		y_xe3a=random.randint(-1060,-460)
		score+=lv
		y_velocity+=spend_up
		pygame.mixer.Sound.play(sound1)
	if y_xe4a >600:	
		x_xe4a=random.randint(500,560)
		y_xe4a=random.randint(-1060,-460)
		score+=lv
		y_velocity+=spend_up
		pygame.mixer.Sound.play(sound1)	
	if score>100 and lv == 1:
		spend_up = 0
	if score>160 and lv == 2:
		spend_up = 0
	if score>220 and lv == 3:
		spend_up = 0
	if score>280 and lv == 4:
		spend_up = 0
	if score>340 and lv == 5:
		spend_up = 0			
	# Vẽ viền và điểm
	pygame.draw.rect(screen , RED,(190,y_ray_do - 100,10,50))
	pygame.draw.rect(screen , RED,(190,y_ray_do,10,50))
	pygame.draw.rect(screen , RED,(190,y_ray_do + 100,10,50))
	pygame.draw.rect(screen , RED,(190,y_ray_do + 200,10,50))
	pygame.draw.rect(screen , RED,(190,y_ray_do + 300,10,50))
	pygame.draw.rect(screen , RED,(190,y_ray_do + 400,10,50))
	pygame.draw.rect(screen , RED,(190,y_ray_do + 500,10,50))
	pygame.draw.rect(screen , RED,(600,y_ray_do - 100,10,50))
	pygame.draw.rect(screen , RED,(600,y_ray_do,10,50))
	pygame.draw.rect(screen , RED,(600,y_ray_do + 100,10,50))
	pygame.draw.rect(screen , RED,(600,y_ray_do + 200,10,50))
	pygame.draw.rect(screen , RED,(600,y_ray_do + 300,10,50))
	pygame.draw.rect(screen , RED,(600,y_ray_do + 400,10,50))
	pygame.draw.rect(screen , RED,(600,y_ray_do + 500,10,50))
	
	x1=pygame.draw.rect(screen , COL1,(x_xe1,y_xe1,40,50))
	x2=pygame.draw.rect(screen , COL2,(x_xe2,y_xe2,40,50))
	x3=pygame.draw.rect(screen , COL3,(x_xe3,y_xe3,40,50))
	x4=pygame.draw.rect(screen , COL4,(x_xe4,y_xe4,40,50))
	x5=pygame.draw.rect(screen , COL5,(x_xe1a,y_xe1a,40,50))
	x6=pygame.draw.rect(screen , COL6,(x_xe2a,y_xe2a,40,50))
	x7=pygame.draw.rect(screen , COL7,(x_xe3a,y_xe3a,40,50))
	x8=pygame.draw.rect(screen , COL8,(x_xe4a,y_xe4a,40,50))

	pygame.draw.rect(screen , ORANGE,(650,500,120,40))
	pygame.draw.rect(screen , GREEN,(640,55,90,40))
	pygame.draw.rect(screen , GREEN,(750,55,40,40))
	pygame.draw.rect(screen , GREEN,(730,120,20,20))
	pygame.draw.rect(screen , GREEN,(770,120,20,20))

	if y_ray_do -100>0 :
		y_ray_do = 0
	
	car_rect = pygame.draw.rect(screen , PINK,(x_car,y_car,30,30))	
	if nhan:
		x_car = mouse_x -15
		y_car = mouse_y -15
	# Chạm biên
	if car_rect.colliderect(x1):
		nhan = False
		start  = False
		gameover = True	
	if car_rect.colliderect(x2):
		nhan = False
		start  = False
		gameover = True		
	if car_rect.colliderect(x3):
		nhan = False
		start  = False
		gameover = True	
	if car_rect.colliderect(x4):
		nhan = False
		start  = False
		gameover = True	
	if car_rect.colliderect(x5):
		nhan = False
		start  = False
		gameover = True	
	if car_rect.colliderect(x6):
		nhan = False
		start  = False
		gameover = True	
	if car_rect.colliderect(x7):
		nhan = False
		start  = False
		gameover = True	
	if car_rect.colliderect(x8):
		nhan = False
		start  = False
		gameover = True	
	if car_rect.colliderect(bien1_rect):
		nhan = False
		start  = False
		gameover = True								
	if car_rect.colliderect(bien2_rect):
		nhan = False
		start = False
		gameover = True
	myscore_txt =sfont1.render("Score:"+str(score), True ,ORANGE)	
	gameover_txt =sfont3.render("GAMEOVER!", True ,BLUE)
	choilai_txt =sfont2.render("Reset", True ,PINK)
	h_txt =sfont7.render("Make by Hieus", True ,RED)
	hieu_txt =sfont8.render("HIẾU VIJ_PRO ", True ,RED)
	start_txt =sfont4.render("START", True ,ORANGE)
	lever_txt = sfont5.render("Độ khó:    " +str(lv), True, ORANGE)
	cong_txt =sfont6.render("+", True ,BLACK)
	tru_txt =sfont4.render("-", True ,BLACK)
	screen.blit(choilai_txt,(660,510))
	screen.blit(myscore_txt,(20,500))
	screen.blit(lever_txt,(645,65))
	screen.blit(tru_txt,(730,112))
	screen.blit(cong_txt,(770,114))
	screen.blit(h_txt,(1,1))
	if gameover :
		screen.blit(gameover_txt,(215,200))
		lock = True
		pygame.mixer.Sound.play(sound2)
		
	if start == False and lock == False:
		pygame.draw.rect(screen , choice(aray),(300,490,200,70))	
		screen.blit(start_txt,(343,505))
	if score>100:
		screen.blit(hieu_txt,(1,100))		
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button ==1:
				if lock == False:
					if 300<=mouse_x<=500 and 490<=mouse_y<=560:
						start =True	
						nhan = True	
				if 650<=mouse_x<=770 and 500<=mouse_y<=540:
						stop = True
						pygame.mixer.stop()
						if stop:
							x_velocity = 1
							y_velocity = 1
							y_ray_do = 0
							score = 0
							x_car = 380
							y_car = 520
							x_xe1=random.randint(200,250)
							y_xe1=random.randint(-500,0)
							x_xe2=random.randint(300,350)
							y_xe2=random.randint(-500,0)
							x_xe3=random.randint(400,450)
							y_xe3=random.randint(-500,0)
							x_xe4=random.randint(500,550)
							y_xe4=random.randint(-500,0)
							x_xe1a=random.randint(200,250)
							y_xe1a=random.randint(-1060,-560)
							x_xe2a=random.randint(300,350)
							y_xe2a=random.randint(-1060,-560)
							x_xe3a=random.randint(400,450)
							y_xe3a=random.randint(-1060,-560)
							x_xe4a=random.randint(500,550)
							y_xe4a=random.randint(-1060,-560)
							nhan = False
							running = True
							start = False
							stop = False
							gameover = False
							
							lock = False
				if 730<=mouse_x<=750 and 120<=mouse_y<=140:	
					if 1<lv<=5:
						lv -=1
						spend_up -=0.02	
				if 770<=mouse_x<=790 and 120<=mouse_y<=140:
					if 1<=lv<5:
						lv+=1
						spend_up +=0.02
	pygame.display.flip()
pygame.quit()