import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n+1)]
route = [-1 for _ in range(n+1)]

for i in range(n):
  for j in range(i):
    if arr[i] > arr[j]:
      tmp = dp[i]
      dp[i] = max(dp[i], dp[j]+1)
      if dp[i] != tmp:
        route[i] = j

idx = dp.index(max(dp))
dq = deque([])
while idx >= 0:
  dq.appendleft(arr[idx])
  idx = route[idx]

print(max(dp))
while dq:
  print(dq.popleft(), end=" ")
