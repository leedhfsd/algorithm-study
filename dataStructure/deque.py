#덱 구현, 덱은 원형 큐와 같다. push_front를 하면 배열의 뒤 인덱스에 넣는 것.
#push_front 할 때 front = (front - 1 + MAX_QUEUE_SIZE) % MAX_QUEUE_SIZE 
MAX_QUEUE_SIZE = 100000
class Deque:
  def __init__(self):
    self.front = 0
    self.back = 0
    self.size = 0
    self.queue = [0] * MAX_QUEUE_SIZE

  def push_front(self, value):
    self.queue[self.front] = value
    self.front = (self.front - 1 + MAX_QUEUE_SIZE) % MAX_QUEUE_SIZE
    self.size += 1
  
  def push_back(self, value):
    self.back = (self.back + 1) % MAX_QUEUE_SIZE
    self.queue[self.back] = value
    self.size += 1
  
  def print_size(self):
    print(self.size)
    return
  
  def print_front(self):
    if self.size > 0:
      print(self.queue[(self.front + 1) % MAX_QUEUE_SIZE])
      return
    else:
      print(-1)
      return
  
  def print_back(self):
    if self.size > 0:
      print(self.queue[self.back])
      return
    else:
      print(-1)
      return

  def empty(self):
    if self.size == 0:
      print(1)
      return
    else:
      print(0)
      return

  def pop_front(self):
    if self.size == 0:
      print(-1)
      return
    else:
      self.front = (self.front + 1) % MAX_QUEUE_SIZE
      print(self.queue[self.front])
      self.size -= 1
      return

  def pop_back(self):
    if self.size == 0:
      print(-1)
      return
    else:
      print(self.queue[self.back])
      self.back = (self.back-1+MAX_QUEUE_SIZE) % MAX_QUEUE_SIZE
      self.size -= 1
      return
