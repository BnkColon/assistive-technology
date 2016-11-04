import pyautogui
import pygame, sys, os

pygame.init()

# ancho y altura de la pantalla
width, height = pyautogui.size()

gameExit= False

pyautogui.FAILSAFE = True

pygame.display.gl_set_attribute(pygame.GL_ALPHA_SIZE,8)
gameDisplay= pygame.display.set_mode((900,900)) #pygame.NOFRAME
pygame.display.set_caption('Demo')
pygame.display.init()

RED= (255, 0, 0)
WHITE= (255, 255, 255)

pygame.display.update()
gameExit= False

# guarda todos los eventos
ev = pygame.event.get()

pos_x = 0
pos_y = 0

print('Press Ctrl-C to quit.')

try:
    while not gameExit:
        for x in range(0, width, 10):
            pyautogui.moveTo(x, height/2, duration= .01)
            for event in pygame.event.get():
                if event.type == 5 or event.type == 6:
                    if event.button == 1:
                          pos_x = x
                          x = width
                          break
                    break
                break
            if(x == width):
                break
        for y in range(0, height, 10):
            pyautogui.moveTo(pos_x, y, duration= .01)
            for event in pygame.event.get():
                if event.type == 5:
                    #print("entre")
                    if event.button == 1:
                        #print("got y")
                        pos_y = y
                        y = height
                        #pygame.display.quit()
                        break
                    break
                break
            if(y == height):
                pygame.display.quit()
                break
            
            
            
        #click en pos_x y pos_y
        pyautogui.doubleClick(pos_x, pos_y)
        print("x = %d, y = %d" %(pos_x, pos_y))
        
        
        gameExit = True
        
except KeyboardInterrupt:
    print('\n')


pygame.quit()
quit()
