import sys
from collections import defaultdict
input = sys.stdin.readline

log = defaultdict(list)
tc = int(input())
for _ in range(tc):
  name, status = input().rstrip().split()
  if status != "enter" and status != "leave":
    continue
  log[name].append(status)
ans = []
for k, v in log.items():
  enter, leave = -1, -1
  for i in range(len(v)):
    if v[i] == "enter":
      enter = i
    elif v[i] == "leave":
      leave = i
  if enter > leave:
    ans.append(k)

ans.sort(reverse=True)
for i in ans:
  print(i)
