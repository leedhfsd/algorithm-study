import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque([i for i in range(1, n+1)])
res = ""
while len(dq) > 1:
  res = res + str(dq.popleft()) + " "
  tmp = dq.popleft()
  dq.append(tmp)

print(res + str(dq[0]))
