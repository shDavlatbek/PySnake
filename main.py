# '''
# Class Private vars, funcs
# '''

# '''
#   params:LO
#   return:LO
# '''

# class Private:
#   def __init__(self):
#     self.__privateVar = 0
#     self.publicVar = 1

#   def __privateFunc(self):
#     print(self.__privateVar)

#   def publicFunc(self):
#     print(self.publicVar)
#     self.__privateFunc()


# obj = Private()

# obj.publicFunc()

# #obj.__privateFunc() #error


# '''

# __slots__
# secury the variable

# '''

import os
import time
import keyboard
import copy
from py_snake import Snake

def print_con(txt):
  os.system('cls')
  print(txt)


snake = Snake(0)

x = 1
y = 1

field_size = 20

def game_over(txt, score):
  print_con('')
  time.sleep(0.5)
  print_con(txt)
  time.sleep(0.5)
  print_con('')
  time.sleep(0.5)
  print_con('')
  time.sleep(0.5)
  print_con(txt)
  time.sleep(0.5)
  print_con('')
  time.sleep(0.5)
  print_con(
f'''



                      ____                        ___
                    / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __
                    | |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
                    | |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |
                    \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|
              
                                  Score: {score}



'''
  )
  
  

def on_arrow_up(e):
    if e.event_type == keyboard.KEY_DOWN:
      if cant_turn == 'up':
        snake.setdirection('down')
      else: snake.setdirection('up')

def on_arrow_down(e):
    if e.event_type == keyboard.KEY_DOWN:
      if cant_turn == 'down':
        snake.setdirection('up')
      else: snake.setdirection('down')

def on_arrow_right(e):
    if e.event_type == keyboard.KEY_DOWN:
      if cant_turn == 'right':
        snake.setdirection('left')
      else: snake.setdirection('right')

def on_arrow_left(e):
    if e.event_type == keyboard.KEY_DOWN:
      if cant_turn == 'left':
        snake.setdirection('right')
      else: snake.setdirection('left')

keyboard.on_press_key("up", on_arrow_up)
keyboard.on_press_key("down", on_arrow_down)
keyboard.on_press_key("right", on_arrow_right)
keyboard.on_press_key("left", on_arrow_left)

snake_size = [[1,1], [1,2], [1,3]]
food = snake.setrandomdot(snake.create_field(field_size),field_size, ' • ', snake_size)

global cant_turn
cant_turn = ''

over = False

while True:
  
  if over:
    game_over(frame, snake.getscore())
    break
  
  key_name = snake.getdirection()
  
  x_b = x
  y_b = y
    
  if key_name == 'right':
    dot = ' ▶ '
    x += 1
    cant_turn = 'left'
    if x >= field_size:
      x = 1
      
  elif key_name == 'left':
    dot = ' ◀ '
    x -= 1
    cant_turn = 'right'
    if x <= 0:
      x = field_size
    
  elif key_name == 'up':
    dot = ' ▲ '
    y -= 1
    cant_turn = 'down'
    if y <= 0:
      y = field_size
      
  elif key_name == 'down':
    dot = ' ▼ '
    y += 1
    cant_turn = 'up'
    if y > field_size:
      y = 1        
  
  
  snake_size.insert(0, list([x, y]))
  if food[1] == x and food[2] == y:
    snake.addscore(1)
    food = snake.setrandomdot(work_field, field_size, ' • ', snake_size)
  else:
    snake_size.pop()
      
  
  work_field = snake.setdot(food[1], food[2], snake.create_field(field_size), ' • ')
  for key,i in enumerate(snake_size):
    if key == 0:
      work_field = snake.setdot(i[0], i[1], work_field, dot)
      continue
    work_field = snake.setdot(i[0], i[1], work_field, ' ■ ')
    
  frame = ''
  
  for row in work_field:
    frame += ''.join(row)
    frame += '\n'    
  frame += 'Score: ' + str(snake.getscore())
  print_con(frame)
  
  while [x, y] in snake_size[1:]: 
    
    over = True
    break
  
  time.sleep(0.1)
  
