a = list(input())
b = list(input())

dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
for i in range(1,len(a)+1):
  for j in range(1,len(b)+1):
    if a[i-1] == b[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

x, y = len(a), len(b)
res = ""
print(dp[len(a)][len(b)])
if dp[len(a)][len(b)] > 0:
  while x > 0 and y > 0:
    if dp[x-1][y] == dp[x][y]:
      x -= 1
      continue
    if dp[x][y-1] == dp[x][y]:
      y -= 1
      continue
    if dp[x-1][y-1] + 1 == dp[x][y]:
      res = b[y-1] + res
      x -= 1
      y -= 1
  print(res)
