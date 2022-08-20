import sys
from collections import defaultdict
input = sys.stdin.readline
INF = sys.maxsize
v, e = map(int,input().split())
graph = defaultdict(list)

def bf():
  dist = [INF for _ in range(v+1)]
  dist[1] = 0
  flag = False
  for i in range(v):
    for j in range(1, v+1):
      for nxt, dis in graph[j]:
        if dist[nxt] > dist[j] + dis and dist[j] != INF:
          dist[nxt] = dist[j] + dis
          if i == v-1:
            flag = True
  
  if not flag:
    tmp = dist[2:]
    for i in tmp:
      if i != INF:
        print(i)
      else:
        print(-1)
  else:
    print(-1)
  
for _ in range(e):
  start, end , dis = map(int,input().split())
  graph[start].append((end, dis))
  
bf()
