import random
class Snake:
  def __init__(self, score, direction:str = 'right') -> None:
    self.score = score
    self.direction = direction
  
  @staticmethod
  def create_field(size: int) -> list:
    gamefield = []
    for i in range(size):
      if i == 0:
        l = ['+'] + ['---' for i in range(size)] + ['+']
        gamefield.append(l)

      l = ['|'] + ['   ' for i in range(size)] + ['|']
      gamefield.append(l)

      if i == size - 1:
        l = ['+'] + ['---' for i in range(size)] + ['+']
        gamefield.append(l)

    return gamefield
  
  @staticmethod
  def setdot(x:int, y:int, field:list, dot:str) -> list:
    field[y][x] = dot
    return field
  
  @staticmethod
  def setrandomdot(field:list, size:int, dot:str, exclude:list = []) -> (list, int, int):
    x = random.randint(1, size - 2)
    y = random.randint(1, size - 2)
    while (x, y) in exclude:
      x = random.randint(1, size - 2)
      y = random.randint(1, size - 2)
    field[y][x] = dot
    return field, x, y
  
  def if_eat(x:int, y:int, field:list, dot:str) -> bool:
    if field[x][y] == dot:
      return True
    return False
  
  def addscore(self, score:int) -> None:
    self.score += score
    
  def getscore(self) -> int:
    return self.score
  
  def setdirection(self, direction):
    self.direction = direction
    
  def getdirection(self) -> str:
    return self.direction