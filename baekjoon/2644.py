import sys
from collections import defaultdict
input = sys.stdin.readline

graph = defaultdict(list)
n = int(input())
visited = [0 for _ in range(n+1)]
start, end = map(int,input().split())
edge = int(input())
ans = 0
for _ in range(edge):
  parent, child = map(int,input().split())
  graph[parent].append(child)
  graph[child].append(parent)


def dfs(pos, res):
  global end, visited, ans
  visited[pos] = 1
  if pos == end:
    ans = res
    return ans
  for i in graph[pos]:
    if not visited[i]:
      dfs(i, res+1)

dfs(start,0)

if ans:
  print(ans)
else:
  print(-1)
