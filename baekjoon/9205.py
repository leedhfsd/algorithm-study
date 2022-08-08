import sys
from collections import defaultdict
input = sys.stdin.readline
tc = int(input())

def dfs(start):
  global graph
  for i in graph[start]:
    if not visited[i]:
      visited[i] = 1
      dfs(i)

for _ in range(tc):
  n = int(input())
  graph = defaultdict(list)
  home = list(map(int,input().split()))
  cv = []
  for _ in range(n):
    cv.append(list(map(int,input().split())))
  end = list(map(int,input().split()))

  if abs(home[0] - end[0]) + abs(home[1] - end[1]) <= 1000:
    graph[0].append(n+1)
    graph[n+1].append(0)

  for i in range(n):
    x1, y1 = cv[i] 
    if abs(x1-home[0]) + abs(y1-home[1]) <= 1000:
      graph[0].append(i+1)
      graph[i+1].append(0)
    if abs(x1-end[0]) + abs(y1-end[1]) <= 1000:
      graph[n+1].append(i+1)
      graph[i+1].append(n+1)
    for j in range(n):
      if i == j: continue
      x2, y2 = cv[j]
      if abs(x1-x2) + abs(y1-y2) <= 1000:
        graph[i+1].append(j+1)
  visited = [0 for _ in range(n+2)]
  visited[0] = 1
  dfs(0)
  if visited[-1] == 1:
    print("happy")
  else:
    print("sad")
