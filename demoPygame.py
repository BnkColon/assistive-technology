import pyautogui
import pygame

pygame.init()

# ancho y altura de la pantalla
width, height = pyautogui.size()

gameDisplay= pygame.display.set_mode((800,600))
pygame.display.set_caption('Demo')

pygame.display.init()

# x= pygame.display.get_surface()
# print (x)

RED= (153, 0, 0)
pygame.display.update()

gameExit= False
x= 300
y= 300

# guarda todos los eventos
ev = pygame.event.get()

while not gameExit:
	for event in ev:
		if event.type == pygame.QUIT:
			gameExit= True 
		if event.type == pygame.KEYDOWN: 
			if event.type == pygame.K_LEFT:
				#...
			if event.type == pygame.K_RIGHT:
				#...

	pygame.draw.line(gameDisplay, RED, (45,20), (45,30), 4)
	pygame.display.update()




pygame.display.quit()
pygame.quit()

quit()
