import sys
input = sys.stdin.readline

n = int(input())
arr = [0,0,0]
for _ in range(n):
  arr.append(int(input()))

dp = [0,0,0] + [0 for _ in range(n)]


for i in range(3, n+3):
  dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])
  dp[i] = max(dp[i], dp[i-1])

print(max(dp))
