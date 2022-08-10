import sys
from collections import defaultdict
input = sys.stdin.readline

num, party = map(int,input().split())
truth_people = set(list(map(int,input().split()))[1:])
ans = 0

def dfs(start):
  for i in graph[start]:
    if not visited[i]:
      visited[i] = 1
      dfs(i)

info = []
graph = defaultdict(list)
visited = [0 for _ in range(num+1)]
for _ in range(party):
  tmp = list(map(int,input().split()))[1:]
  info.append(tmp)

  for i in range(len(tmp)):
    for j in range(len(tmp)):
      if i == j: continue
      graph[tmp[i]].append(tmp[j])

for i in truth_people:
  if not visited[i]:
    visited[i] = 1
    dfs(i)

for i in range(len(info)):
  flag = False
  for j in info[i]:
    if visited[j]:
      flag = True
      break
  if not flag:
    ans += 1

print(ans)
