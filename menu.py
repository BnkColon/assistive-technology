import pyautogui
from pynput.mouse import Listener, Button as ButtonPynput
from tkinter import *

pyautogui.FAILSAFE = False 

global VelocityVar

def sel(self):
  global VelocityVar
  VelocityVar = var.get()

#GUI
root = Tk()
var = IntVar()

scale = Scale( root, variable = var, from_= 1, to= 10, orient= HORIZONTAL, label = "velocity", command = sel)
scale.pack(anchor=CENTER)

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

velocities = [(0,.25), (0,.10), (0,.1), (5,.25), (5,.10), (5,.1), (10,.25), (10,.10), (10,.1), (15,.10), (15,.1)]
speedInput= 0


def velocity(x):
  print (" v", velocities)
  print (" x", x)
  print ("val: " , velocities[x])
  val = velocities[x]
  jump = val[0]
  duration = float(val[1])
  print("duration, jump, val:", duration, jump, val)
  return jump, duration

#variables
#velocity
print (" VV", VelocityVar)
jump, duration = velocity(VelocityVar)
print("jump = %d, duration = %d" %(jump, duration))

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

      print(pos_x)

      if pos_x != 0:
        listener.stop()
        break

    click= True
  

  #click en pos_x y pos_y
  pyautogui.doubleClick(pos_x, pos_y)
  pyautogui.doubleClick(pos_x, pos_y)
  exit= True
  print("x = %d, y = %d" %(pos_x, pos_y))

