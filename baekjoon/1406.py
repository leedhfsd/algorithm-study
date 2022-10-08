import sys
from collections import deque
input = sys.stdin.readline

inp = list(input().rstrip())
left = deque(inp)
right = deque([])

n = int(input())
for _ in range(n):
  op = input().rstrip()
  if op == "L":
    if len(left) > 0:
      right.appendleft(left.pop())
  elif op == "D":
    if len(right) > 0:
      left.append(right.popleft())
  elif op == "B":
    if len(left) > 0:
      left.pop()
  else:
    oper, val = op.split()
    left.append(val)

ans = left + right
print("".join(ans))

# 연결리스트로 구현
import sys
input = sys.stdin.readline

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
  
  def insert(self, pos, data):
    tmp = pos.prev
    new_node = Node(data, tmp, pos)
    pos.prev = new_node
    tmp.next = new_node

  def delete(self, pos):
    tmp_prv = pos.prev
    tmp_nxt = pos.next
    tmp_prv.next = tmp_nxt
    tmp_nxt.prev = tmp_prv  

  def print(self):
    cur = self.head.next
    while cur != self.tail:
      if cur != self.tail:
        print(cur.data, end="")
      else:
        print(cur.data)
      cur = cur.next

word = list(input().rstrip())
n = int(input())
lis = dList()
cur = lis.tail
for i in range(len(word)):
  lis.insert(cur, word[i])

for _ in range(n):
  op = input().rstrip().split()
  if op[0] == "L":
    if cur.prev.prev != None:
      cur = cur.prev
  elif op[0] == "D":
    if cur.next != None:
      cur = cur.next
  elif op[0] == "B":
    if cur.prev.prev != None:
      lis.delete(cur.prev)
  else:
    lis.insert(cur, op[1])

lis.print()
