#! python3
import pyautogui, sys


# ancho y altura de la pantalla
width, height = pyautogui.size()

pyautogui.moveTo(5,5)
half = height/2

for x in range(0, height):
	pyautogui.moveRel(height, 0, duration=0.45)
	if pyautogui.click() == True:
		pyautogui.moveRel(0, width, duration=0.45)
	

