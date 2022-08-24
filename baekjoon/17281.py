import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
record = [list(map(int,input().split())) for _ in range(n)]
ans = 0
perm = permutations(range(1,9),8)

for i in set(perm):
  order = list(i[:3]) + [0] + list(i[3:])
  res = 0
  idx = 0
  score = 0
  for i in range(n):
    base_1, base_2, base_3 = 0, 0, 0
    out = 0
    while out < 3:
      cur_num = order[idx]
      if record[i][cur_num] == 0:
        out += 1
        if out == 3:
          idx = (idx + 1) % 9
          break
      elif record[i][cur_num] == 1:
        score += base_3
        base_1, base_2, base_3 = 1, base_1, base_2
      elif record[i][cur_num] == 2:
        score += base_2 + base_3
        base_1, base_2, base_3 = 0, 1, base_1
      elif record[i][cur_num] == 3:
        score += base_1 + base_2 + base_3
        base_1, base_2, base_3 = 0, 0, 1
      elif record[i][cur_num] == 4:
        score += base_1 + base_2 + base_3 + 1
        base_1, base_2, base_3 = 0,0,0
      
      idx = (idx + 1) % 9 
  
  if ans < score:
    ans = score
print(ans)
