import sys
input = sys.stdin.readline

v = int(input())
e = int(input())

dist = [[sys.maxsize for _ in range(v)] for _ in range(v)]
for i in range(v):
  for j in range(v):
    if i == j:
      dist[i][j] = 0

for _ in range(e):
  a, b, dis = map(int,input().split())
  if dist[a-1][b-1] > dis:
    dist[a-1][b-1] = dis

for k in range(v):
  for i in range(v):
    for j in range(v):
      dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

for i in range(v):
  for j in range(v):
    if dist[i][j] == sys.maxsize:
      dist[i][j] = 0
    print(dist[i][j], end=" ")
  print()
