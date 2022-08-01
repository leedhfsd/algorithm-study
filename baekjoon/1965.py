import sys
input = sys.stdin.readline

n = int(input())
inp = list(map(int,input().split()))

dp = [1 for _ in range(n)]
for i in range(1, len(inp)):
  for j in range(i):
    if inp[i] > inp[j]:
      dp[i] = max(dp[j]+1, dp[i])

print(max(dp))
