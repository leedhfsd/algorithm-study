import sys
from collections import defaultdict
input = sys.stdin.readline
n = list(input().rstrip())

count = defaultdict(lambda: 0)
for i in range(len(n)):
  count[int(n[i])] += 1

most = [k for k,v in count.items() if v == max(count.values())]

flag = False
res = 0
for i in most:
  if i != 6 and i != 9:
    res = count[i]
    flag = True
    break

if flag:
  print(res)
else:
  diff = abs(count[6]-count[9]) // 2
  res = max(count[6], count[9]) - diff
  print(res)
