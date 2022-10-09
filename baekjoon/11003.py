from collections import deque
n, l = map(int,input().split())
num = list(map(int,input().split()))
dq = deque([])
for i in range(n):
  while dq and dq[-1] > num[i]:
    dq.pop()
  dq.append(num[i])

  #여기서 L개 전까지의 범위 유지
  if i >= l and dq[0] == num[i-l]:
    dq.popleft()
  print(dq[0],end=" ")
