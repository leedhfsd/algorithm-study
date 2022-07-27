import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int,input().split()))
cost = list(map(int,input().split()))

dis = 0
idx = 0
res = 0
for i in range(n-1):
  if cost[idx] <= cost[i]:
    dis += dist[i]
  else:
    res += dis * cost[idx]
    dis = dist[i]
    idx = i

res = res + dis * cost[idx]
print(res)
