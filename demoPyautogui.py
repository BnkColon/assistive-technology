import pyautogui


# ancho y altura de la pantalla
width, height = pyautogui.size()

pyautogui.FAILSAFE = True
for x in range(0, width):
	pyautogui.moveTo(x, height/2)

