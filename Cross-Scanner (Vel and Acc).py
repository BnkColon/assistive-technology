# Cross-Scanner		16/diciembre/2016
# Software Engineering Project
# Participants:
# 	Valerie Santiago
# 	Lillian Gonzalez
# 	Maria Lopez
# 	Bianca Colon
# 	Javier Rodriguez


import pyautogui
from pynput.mouse import Listener, Button as ButtonPynput
from tkinter import *

pyautogui.FAILSAFE = False

#variable para velocidad
global VelocityVar
#variable para aceleracion
global AcelerationVar
#variable para determinar de cuanto en cuanto pixeles se va a mover el cursor
global jump

#funciones que reciben el valor dado por el GUI y lo
#guardan en sus respectivas variables globales
def sel(self):
	global VelocityVar
	VelocityVar = var.get()

def sel2(self):
	global AcelerationVar
	AcelerationVar = var2.get()

#GUI
root = Tk()
var = IntVar()
var2 = IntVar()

#escala de velocidad
scale = Scale( root, variable = var, from_= 1, to= 5, orient= HORIZONTAL, label = "velocidad", command = sel)
scale.pack(anchor=CENTER)

#escala de aceleracion
scale2 = Scale( root, variable = var2, from_= 0, to= 5, orient= HORIZONTAL, label = "aceleracion", command = sel2)
scale2.pack(anchor=CENTER)

label = Label(root)
label.pack()

root.mainloop()
#end GUI


#funcion que separa el par ordenado de la lista de velocidades y
#las asigna a sus respectivas variables

#funcion para determinar la velocidad del cursor
def velocity(x):
	global jump
	#separar par ordenado que contiene la variable duracion de MoveRel y el jump
	val = velocities[x-1]
	jump = val[0]
	duration = float(val[1])
	return jump, duration


#funcion que determina los cambios en el jump de acuerdo a la aceleracion
#seleccionada en el GUI
def acelerationFunction(acelerationVar, itere):
	global jump
	if(acelerationVar == 1):
		if(itere%15 == 0):
			jump += 1
	if(acelerationVar == 2):
		if(itere%10 == 0):
			jump += 1
	if(acelerationVar == 3):
		if(itere%5 == 0):
			jump += 1
	if(acelerationVar == 4):
		if(itere%3 == 0):
			jump += 1
	if(acelerationVar == 5):
		if(itere%3 == 0):
			jump += 2
	return jump



# variables globales para determinar direccion del scanner
global hold, up, down, right, left
down= False
up= False
right= False
left= False

#capturacion del click
global click, exit, start, finish
click= False
exit= False
start= True
finish= False


# funcion de capturar el x del click
def on_clickX(x, y, button, pressed):
	if button == ButtonPynput.left:
		global pos_x
		pos_x = x
	if button == ButtonPynput.right:
		global hold
		hold =True
	return True

# funcion de capturar la y del click
def on_clickY(x, y, button, pressed):
	if button == ButtonPynput.left:
		global pos_y
		pos_y = y
	if button == ButtonPynput.right:
		global hold
		hold = True
	return True

# funcion para determinar la direccion vertical del escaner (hacia arriba o abajo)
def on_click_Vertical(x, y, button, pressed):
	if button == ButtonPynput.left:
		global down
		down = True
	elif button == ButtonPynput.right:
		global up
		up = True
	return True

# funcion para determinar la direccion horizontal del escaner (hacia la derecha o izquierda)
def on_click_Horizontal(x, y, button, pressed):
	if button == ButtonPynput.left:
		global right
		right = True

	elif button == ButtonPynput.right:
		global left
		left = True
	return True

# funcion para devolver las variables globales a sus estados originales
# con proposito de volver el escaner al principio
def reset():
	global down, up, left, right
	down = False
	up = False
	right = False
	left = False

	global click, exit, start, finish
	click = False
	exit = False
	start = True
	finish = False

	global pos_x, pos_y
	pos_x = 0
	pos_y = 0

	return True



# principio del main

#variables para ancho y altura de la pantalla
width, height = pyautogui.size()

#coordenadas para el click inicializadas a 0 (o sea no se ha escojido la posicion deseada todavia)
global pos_x, pos_y
pos_x = 0
pos_y = 0

#lista de velocidades
	#mientras mas grande la parte entera, mas rapido
	#mientras mas pequena la parte decimal, mas rapido
velocities = [(10,.10), (12,.10), (15,.10), (17,.10), (20,.10)]

#lista de aceleractiones
acelerations = [0,1,2,3,4,5]

#variables de velocidad
jump1, duration = velocity(VelocityVar)
jump = jump1

# main
while not exit:
	while not click:
		while start:
			# mueve el cursor al medio de la pantalla
			pyautogui.moveTo(width/2, height/2)

			# registra los clicks
			listener = Listener(on_click= on_click_Vertical)
			listener.start()

			if down == True:
				# cursor se mueve de la mitad de la pantalla hacia abajo
				y = height/2
				itere = 0

				while(y <= height):
					# print("down")
					y += jump

					#aplicar la aceleracion (de la seleccion del GUI)
					jump = acelerationFunction(AcelerationVar, itere)

					#mover el cursor (relativo a su posicion actual con la duracion determinada por la seleccion en el GUI)
					pyautogui.moveTo(width/2, y, duration= duration)

					#llamar funcion que recibe click en y
					listener = Listener(on_click= on_clickY)
					listener.start()

					#si tenemos la posicion y, salir del while
					if pos_y != 0:
						listener.stop()
						y = height + 1
						print(right, left, down, up, pos_y)
						start=False
						finish=True

			elif up == True:
				# cursor se mueve de la mitad de la pantalla hacia arriba
				y = height/2
				itere = 0

				while(y >= 0):
					y -= jump

					#aplicar la aceleracion (de la seleccion del GUI)
					jump = acelerationFunction(AcelerationVar, itere)

					#mover el cursor (relativo a su posicion actual con la duracion determinada por la seleccion en el GUI)
					pyautogui.moveTo(width/2, y, duration= duration)

					#llamar funcion que recibe click en y
					listener = Listener(on_click= on_clickY)
					listener.start()

					#si tenemos la posicion y, salir del while
					if pos_y != 0:
						listener.stop()
						y =  -1
						start=False
						finish=True

		while finish:
			# mueve el cursor al medio de la pantalla con la posicion y dada
			pyautogui.moveTo(width/2, pos_y)

			# registra los clicks
			listener = Listener(on_click= on_click_Horizontal)
			listener.start()

			if right == True :
				# print ("right")
				# cursor se mueve horizontalmente de la mitad de la pantalla hacia la derecha
				x = width/2
				itereX = 0

				#reset el jump a la velocidad inicial elegida en el GUI
				jump = jump1
				while(x <= width):
					x += jump

					#aplicar la aceleracion
					jump = acelerationFunction(AcelerationVar, itereX)

					#mover cursor relativo a la posicion del cursor actual
					pyautogui.moveTo(x, pos_y, duration= duration)

					#llamar funcion que recibe click en eje de x
					listener = Listener(on_click= on_clickX)
					listener.start()

					#si tenemos la posicion x, salir del while
					if pos_x != 0:
						listener.stop()
						x = width + 1


			elif left ==True:
				# print ("left")
				# cursor se mueve horizontalmente
				x = width/2
				itereX = 0

				#reset el jump a la velocidad inicial elegida en el GUI
				jump = jump1
				while(x >= 0):
					x -= jump

					#aplicar la aceleracion
					jump = acelerationFunction(AcelerationVar, itereX)

					#mover cursor relativo a la posicion del cursor actual
					pyautogui.moveTo(x, pos_y, duration= duration)

					#llamar funcion que recibe click en eje de x
					listener = Listener(on_click= on_clickX)
					listener.start()

					#si tenemos la posicion x, salir del while
					if pos_x != 0:
						listener.stop()
						x = -1

			if pos_x != 0:
				listener.stop()
				finish=False


		if pos_x != 0 and pos_y != 0:
			listener.stop()
			click= True


	#click en pos_x y pos_y
	pyautogui.doubleClick(pos_x, pos_y)
	pyautogui.doubleClick(pos_x, pos_y)
	exit= True
