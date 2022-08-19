import sys
input = sys.stdin.readline

n, k = map(int,input().split())
dist = [0] + list(map(int,input().split()))

res = 0
ans = 0
for i in range(1, n+1):
  if res + dist[i] > k and res <= k:
    ans = i
    res += dist[i]
    break
  else:
    res += dist[i]

if k > res:
  for i in range(n, 0, -1):
    if res + dist[i] > k and res <= k:
      ans = i
      break
    else:
      res += dist[i]

print(ans)
