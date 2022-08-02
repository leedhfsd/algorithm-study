import sys
input = sys.stdin.readline

n, k = map(int,input().split())
inp = list(map(int,input().split()))
res = sum(inp[0:k])
tmp = [res]
for i in range(n-k):
  tmp.append(tmp[i] - inp[i] + inp[i+k])
  if res < tmp[i] - inp[i] + inp[i+k]:
    res = tmp[i] - inp[i] + inp[i+k]

print(res)
