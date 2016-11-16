import pyautogui
from pynput.mouse import Listener, Button


# ancho y altura de la pantalla
width, height = pyautogui.size()

# coordenadas para el click
pos_x = 0
pos_y = 0

# capturacion del click
click= False

# salida del programa 
exit= False

# funcion de capturar el x del click
def on_clickX(x, y, button, pressed):
	if button== Button.left:
		global pos_x 
		pos_x = x
		return True

# funcion de capturar la y del click 
def on_clickY(x, y, button, pressed):
	if button== Button.left:
		global pos_y
		pos_y = y
		return True


while not exit:
	while not click:
		# cursor se mueve horizontalmente
		for x in range(0, width, 10):
			pyautogui.moveTo(x, height/2, duration= .01) 

			listener = Listener(on_click= on_clickX)
			listener.start()

			#print(pos_x)

			if pos_x != 0:
			listener.stop()
			break

		# cursor se mueve verticalmente
		for y in range(0, height, 10):
			pyautogui.moveTo(pos_x, y, duration= .01)

			listener = Listener(on_click= on_clickY)
			listener.start()

			#print(pos_y)

			if pos_y != 0:
			listener.stop()
			break

			click= True
  

	#click en pos_x y pos_y
	pyautogui.doubleClick(pos_x, pos_y)
	pyautogui.doubleClick(pos_x, pos_y)
	exit= True
	print("x = %d, y = %d" %(pos_x, pos_y))