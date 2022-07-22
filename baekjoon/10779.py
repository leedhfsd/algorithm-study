#막대기의 끝일때는 이전의 char이 )인경우. 
#이 경우는 마지막 끝부분 하나만 더해주면 된다.

import sys
from collections import deque
input = sys.stdin.readline

inp = list(input().rstrip())
dq = deque([])
res = 0

for i in range(len(inp)):
  if inp[i] == "(":
    dq.append("(")
  else:
    if inp[i-1] == "(":
      dq.pop()
      res += len(dq)
    else:
      dq.pop()
      res += 1

print(res)
