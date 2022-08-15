#플로이드 와샬. 간단하니까 외워놓자!!

v, m, e = map(int,input().split())
item = list(map(int,input().split()))
INF = 1000000

dist = [[INF for _ in range(v)] for _ in range(v)]

for i in range(v):
  for j in range(v):
    if i == j:
      dist[i][j] = 0

for _ in range(e):
  a, b, dis = map(int,input().split())
  dist[a-1][b-1], dist[b-1][a-1] = dis, dis

for k in range(v):
  for i in range(v):
    for j in range(v):
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
ans = -1

for i in range(v):
  res = 0
  for j in range(v):
    if dist[i][j] <= m:
      res += item[j]
  if ans < res:
    ans = res

print(ans)
