import sys
from collections import defaultdict
input = sys.stdin.readline

tc = int(input())


for _ in range(tc):
  n, m = map(int,input().split())
  graph = defaultdict(list)
  for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
  print(n-1)
