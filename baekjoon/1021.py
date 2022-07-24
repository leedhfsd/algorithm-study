import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
dq = deque([i for i in range(1, n+1)])
remove = deque(list(map(int,input().split())))
res = 0

for i in remove:
  while dq[0] != i:
    if dq.index(i) <= len(dq) // 2:
      tmp = dq.popleft()
      dq.append(tmp)
      res += 1
    else:
      tmp = dq.pop()
      dq.appendleft(tmp)
      res += 1
  dq.popleft()
print(res)
