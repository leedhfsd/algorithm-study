#트리의 지름은 아무점에서 가장 먼 길이의 노드를 구하고 그 노드에서 다시 최대 거리를 구하면 트리의 지름이다.

import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**9)

v = int(input())
graph = defaultdict(list)
end_point = []
for _ in range(v):
	tmp = list(map(int,input().split()))
	vertex = tmp[0]
	tmp = tmp[1: len(tmp)-1]

	for i in range(0, len(tmp), 2):
		graph[vertex].append((tmp[i], tmp[i+1]))	
	if len(graph[vertex]) == 1:
		end_point.append(vertex)

ans = -sys.maxsize
def dfs(cur, res):
	global ans, flag
	for v, dis in graph[cur]:
		if visited[v] == 0:
			visited[v] = res + dis
			dfs(v, res + dis)

visited = [0 for _ in range(v+1)]
visited[end_point[0]] = -1
dfs(end_point[0], 0)
max_dis = visited.index(max(visited))
visited = [0 for _ in range(v+1)]
visited[max_dis] = -1
dfs(max_dis, 0)
print(max(visited))
