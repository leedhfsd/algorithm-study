import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [0 for _ in range(1502000)]
max_num = 0

for i in range(n):
  days, cost = arr[i]
  max_num = max(max_num, dp[i])
  if i + days > n:
    continue
  dp[i+days] = max(max_num+cost, dp[i+days])
  
print(max(dp))
