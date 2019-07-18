import pygame
from pygame.locals import *
pygame.init()


display_wedith = 640 
display_hight = 480 

game_display = pygame.display.set_mode((display_wedith , display_hight) , 0 , 32 )
pygame.display.set_caption(" caption string  ")


clock = pygame.time.Clock() 
FBS = 30 


while True : 
    for event in pygame.event.get(): 
        if event.type == QUIT : 
            exit()
	''' 
	 	game code 
	
	'''  

        time_passed = clock.tick(FBS)
        time_passed_seconds = time_passed/1000.0	
        game_display.update()
