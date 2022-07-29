import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
  dq_left = deque([])
  dq_right = deque([])
  password = input().rstrip()
  for i in range(len(password)):
    if password[i] == "<":
      if dq_left:
        dq_right.appendleft(dq_left.pop())
    elif password[i] == ">":
      if dq_right:
        dq_left.append(dq_right.popleft())
    elif password[i] == "-":
      if dq_left:
        dq_left.pop()
    else:
      dq_left.append(password[i])
  print("".join(dq_left)+"".join(dq_right))
