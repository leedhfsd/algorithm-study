import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
dist = [0 for _ in range(n+1)]
graph = defaultdict(list)

for _ in range(n-1):
	a, b, dis = map(int,input().split())
	graph[a].append((b,dis))
	graph[b].append((a,dis))

def dfs(start, res):
	for item in graph[start]:
		v, d = item
		if dist[v] == 0:
			dist[v] = res + d
			dfs(v, res + d)

dist[1] = -1
dfs(1, 0)
node = dist.index(max(dist))
dist = [0 for _ in range(n+1)]
dist[node] = -1
dfs(node, 0)
print(max(dist))
