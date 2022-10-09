MAX_QUEUE_SIZE = 10000
class circularQ:
  def __init__(self):
    self.front = 0
    self.back = 0
    self.size = 0
    self.queue = [0] * MAX_QUEUE_SIZE
  
  def empty(self):
    if self.size:
      print("0")
      return
    else:
      print("1")
      return
  
  def print_size(self):
    print(self.size)
    return
  
  def print_front(self):
    if self.size != 0:
      print(self.queue[self.front+1])
    else:
      print(-1)
    return
  
  def print_back(self):
    if self.size != 0:
      print(self.queue[self.back])
    else:
      print(-1)
    return
  
  def push(self, value):
    self.back = (self.back+1) % MAX_QUEUE_SIZE
    self.queue[self.back] = value
    self.size += 1
  
  def pop(self):
    if self.size == 0:
      print(-1)
    else:
      self.front = (self.front+1) % MAX_QUEUE_SIZE
      print(self.queue[self.front])
      self.size -= 1
