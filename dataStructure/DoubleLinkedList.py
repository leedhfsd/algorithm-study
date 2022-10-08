#이중연결리스트 
class Node:
  def __init__(self, data, prev = None, next = None):
    self.data = data
    self.prev = prev
    self.next = next

class dList:
  def __init__(self):
    self.head = Node(None)
    self.tail = Node(None, self.head)
    self.head.next = self.tail
    self.size = 0
  
  def size(self):
    return self.size
  
  def empty(self):
    if self.size:
      return False
    else:
      return True

  def traverse(self, idx):
    if idx > self.size:
      print("Index is over size")
      return None
    elif idx == 0:
      return self.head
    elif idx == self.size:
      return self.tail
    else:
      cur = self.head
      for _ in range(idx):
        cur = cur.next
      return cur

  def insert_left(self, data):
    if self.size == 0:
      self.head = Node(data)
      self.tail = Node(None, self.head)
      self.head.next = self.tail
    else:
      tmp = self.head
      self.head = Node(data, None, tmp);
      tmp.prev = self.head
    self.size += 1
  
  def insert_right(self, data):
    if self.size == 0:
      self.head = Node(data)
      self.tail = Node(None, self.head)
      self.head.next = self.tail
    else:
      tmp = self.tail.prev
      new_node = Node(data, tmp, self.tail)
      tmp.next = new_node
      self.tail.prev = new_node
    self.size += 1
  
  def insert(self, data, idx):
    if self.empty():
      self.head = Node(data)
      self.tail = Node(None, self.head)
      self.head.next = self.tail
    else:
      tmp = self.traverse(idx)
      if tmp == None:
        return
      if tmp == self.head:
        self.insert_left(data)
      elif tmp == self.tail:
        self.insert_right(data)
      else:
        tmp_prev = tmp.prev
        new_node = Node(data, tmp_prev, tmp)
        tmp_prev.next = new_node
        tmp.prev = new_node
    self.size += 1

  def delete(self, idx):
    if self.empty():
      print("List is empty")
      return
    else:
      tmp = self.traverse(idx)
      if tmp == None:
        return
      elif tmp == self.head:
        self.head = tmp.next
      elif tmp == self.tail:
        self.tail = self.tail.prev
      else:
        tmp.prev.next = tmp.next
        tmp.next.prev = tmp.prev
        del(tmp)
      self.size -= 1

  def print(self):
    cur = self.head
    while cur != self.tail:
      if cur.next != self.tail:
        print(cur.data, end="=>")
      else:
        print(cur.data)
      cur = cur.next
