import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)

for _ in range(n-1):
  #부모는 결국 이전의 노드 번호임.
  v1, v2 = map(int,input().split())
  graph[v1].append(v2)
  graph[v2].append(v1)

visited = [0 for _ in range(n+1)]


def dfs(start):
  for node in graph[start]:
    if not visited[node]:
      visited[node] = start
      dfs(node)
dfs(1)
for i in range(2, len(visited)):
  print(visited[i])
