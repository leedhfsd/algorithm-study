# 첫 시도는 bfs로 풀었는데 메모리 부족, 그냥 그리디 느낌으로 품
import sys
input = sys.stdin.readline
a, b = map(int, input().split())
cnt = 0

while a < b:
  if str(b)[-1] == "1":
    b = int(str(b)[0:len(str(b))-1])
    cnt += 1
  elif b % 2 == 0:
    b = int(b / 2)
    cnt += 1
  else:
    break
if a == b:
  print(cnt + 1)
else:
  print(-1)

#bfs로 다시 품
import sys
from collections import deque
input = sys.stdin.readline
a, b = map(int, input().split())
res = 0
flag = False

dq = deque([(a, 0)])

while dq:
  cur, cnt = dq.popleft()
  if cur == b:
    res = cnt
    flag = True
    break

  if cur * 2 <= b:
    dq.append((cur*2, cnt+1))
  if cur * 10 + 1 <= b:
    dq.append((cur*10+1, cnt+1))

if flag: print(res+1)
else: print(-1)
