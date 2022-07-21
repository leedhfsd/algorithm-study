import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())
dq = deque([])
for i in range(n):
  dq.append(i+1)
res = ""

while dq:
  for _ in range(k-1):
    tmp = dq.popleft()
    dq.append(tmp)
  res += str(dq.popleft()) + ", "

print("<"+res[0:-2]+">")
