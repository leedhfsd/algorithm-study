import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))
dp = [1 for _ in range(n+1)]

for i in range(n):
  for j in range(i):
    if number[i] < number[j]:
      dp[i] = max(dp[j]+1, dp[i])

print(max(dp))
