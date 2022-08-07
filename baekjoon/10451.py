import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

tc = int(input())

def dfs(start):
  global visited
  for i in graph[start]:
    if not visited[i]:
      visited[i] = 1
      dfs(i)

for _ in range(tc):
  n = int(input())
  graph = defaultdict(list)
  n_arr = list(map(int,input().split()))
  for i in range(1, len(n_arr)+1):
    graph[i].append(n_arr[i-1])
  
  visited = [0 for _ in range(n+1)]
  res = 0
  for i in range(1, n+1):
    if not visited[i]:
      dfs(i)
      res += 1
  print(res)
