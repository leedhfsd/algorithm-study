import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
  n = int(input())
  stk = [[0]+list(map(int, input().split()))+[0] for _ in range(2)]
  dp = [[0 for _ in range(n+1)] for _ in range(2)]
  
  for i in range(1,n+1):
    dp[0][i] = max(dp[1][i-1] + stk[0][i], dp[0][i-1], dp[1][i-1])
    dp[1][i] = max(dp[0][i-1] + stk[1][i], dp[0][i-1], dp[1][i-1])
  
  print(max(dp[0][n], dp[1][n]))
