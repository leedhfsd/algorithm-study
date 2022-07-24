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
