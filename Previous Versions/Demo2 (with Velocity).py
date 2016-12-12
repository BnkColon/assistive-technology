import pyautogui
from pynput.mouse import Listener, Button as ButtonPynput
from tkinter import *

pyautogui.FAILSAFE = False 

global VelocityVar
global AcelerationVar

def sel(self):
  global VelocityVar
  VelocityVar = var.get()

#def sel2(self):
#  global AcelerationVar
#  AcelerationVar = var2.get()


#GUI
root = Tk()
var = IntVar()

#escala de velocidad
scale = Scale( root, variable = var, from_= 1, to= 5, orient= HORIZONTAL, label = "velocidad", command = sel)
scale.pack(anchor=CENTER)

#escala de aceleracion
#scale = Scale( root, variable = var2, from_= 1, to= 5, orient= HORIZONTAL, label = "aceleracion", command = sel2)
#scale.pack(anchor=CENTER)

label = Label(root)
label.pack()

root.mainloop()
#end GUI

# # ancho y altura de la pantalla
width, height = pyautogui.size()

# # coordenadas para el click
pos_x = 0
pos_y = 0

# # capturacion del click

click= False

exit= False

#mientras mas grande la parte entera, mas rapido
#mientras mas pequena la parte decimal, mas rapido
#velocities =  [(5,.15), (5,.10), (5,.01), (10,.15), (10,.10), (10,.01), (15,.15), (15,.01), (20,.15), (20,.01)]
velocities = [(10,.10), (12,.10), (15,.10), (17,.10), (20,.10)]
speedInput= 0

#lista de aceleractiones
#acelerations = [1,2,3,4,5]


def velocity(x):
  #print (" v", velocities)
  #print (" x", x)
  #print ("val: " , velocities[x-1])
  val = velocities[x-1]
  jump = val[0]
  duration = float(val[1])
  #print("duration, jump, val:", duration, jump, val)
  return jump, duration

#variables
#velocity
#print (" VV", VelocityVar)
jump, duration = velocity(VelocityVar)
#print("jump, duration", jump, duration)

  #bar?
#click is
  #sigle
  #double
  #right

# funcion de capturar el x del click
def on_clickX(x, y, button, pressed):
  if button == ButtonPynput.left:
    global pos_x 
    pos_x = x
  return True

# funcion de capturar la y del click 
def on_clickY(x, y, button, pressed):
  if button== ButtonPynput.left:
    global pos_y
    pos_y = y
  return True

# cursor se mueve horizontalmente
while not exit:
  while not click:
    # cursor se mueve verticalmente
    if(jump == 0):
      jump = 1
    for y in range(0, height, jump):
      pyautogui.moveTo(width/2, y, duration= duration)

      listener = Listener(on_click= on_clickY)
      listener.start()

      #print(pos_y)

      if pos_y != 0:
        listener.stop()
        break

    # cursor se mueve horizontalmente
    for x in range(0, width, jump):
      pyautogui.moveTo(x, pos_y, duration= duration) 

      listener = Listener(on_click= on_clickX)
      listener.start()

      #print(pos_x)

      if pos_x != 0:
        listener.stop()
        break

    click= True
  

  #click en pos_x y pos_y
  pyautogui.doubleClick(pos_x, pos_y)
  pyautogui.doubleClick(pos_x, pos_y)
  exit= True
  #print("x = %d, y = %d" %(pos_x, pos_y))

