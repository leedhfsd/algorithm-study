n, k = map(int, input().split())
coin = []
dp = [0 for _ in range(k+1)]
for _ in range(n):
  inp = int(input())
  coin.append(inp)
dp[0] = 1


for i in coin:
  for j in range(i, k+1):
    if j-i >= 0:
      dp[j] += dp[j-i]

print(dp[k])
