from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
stack = []
res = 0
tmp_res = (0,0)
for _ in range(n):
  tmp = input().rstrip()
  if tmp == "0" and len(stack) > 0:
    tmp_res = stack.pop()
    if tmp_res[1] == 0:
      res += tmp_res[0]
    else:
      if tmp_res[1] - 1 > 0:
        stack.append((tmp_res[0], tmp_res[1]-1))
      elif tmp_res[1] - 1 == 0:
        res += tmp_res[0]
  
  elif tmp != "0":
    trash, score, t = map(int,tmp.split())
    stack.append((score, t))
    tmp_res = stack.pop()

    if tmp_res[1] == 0:
      res += tmp_res[0]
    else:
      if tmp_res[1] - 1 > 0:
        stack.append((tmp_res[0], tmp_res[1]-1))
      elif tmp_res[1] - 1 == 0:
        res += tmp_res[0]
    
print(res)
