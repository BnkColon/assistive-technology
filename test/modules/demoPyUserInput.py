from pymouse import PyMouse
from pykeyboard import PyKeyboard
from pymouse import PyMouseEvent
import pyautogui
from pynput.mouse import Listener, Button

m = PyMouse()
k = PyKeyboard()

# funcion de capturar el click 
def on_click(pressed):
	if pressed:
		return True
	if not pressed:
    	# Stop listener
		return False

# ancho y altura de la pantalla
width, height = pyautogui.size()
# usando pymouse
x_dim, y_dim = m.screen_size()

print('Press Ctrl-C to quit.')

# coordenadas para el click
pos_x = 0
pos_y = 0

# capturacion del click
click= False


try:

	# cursor se mueve horizontalmente
	for x in range(0, width, 10):
		pyautogui.moveTo(x, height/2, duration= .01)

		# collect events
		with Listener() as listener:
			listener.join()  

		#Listener.join()

		if listener.on_click():
        	#click= click()
			pos_x= x
			x = width
			break

		if(x == width):
			break

	for y in range(0, height, 10):
		pyautogui.moveTo(pos_x, y, duration= .01)

		# collect events
		with Listener(on_click=on_click) as listener:
			listener.join()  

		if listener.on_click():
			pos_y = y
			y = height
			break

		if(y == height):
			break
              
            
    #click en pos_x y pos_y
	pyautogui.doubleClick(pos_x, pos_y)
	print("x = %d, y = %d" %(pos_x, pos_y))
          
        
except KeyboardInterrupt:
	print('\n')
