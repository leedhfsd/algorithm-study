import sys
input = sys.stdin.readline
dp = [0 for _ in range(41)]
dp[1], dp[2] = 1, 2
for i in range(3, len(dp)):
  dp[i] = dp[i-2] + dp[i-1]

n = int(input())
m = int(input())
arr = [0 for _ in range(n+1)]
for _ in range(m):
  vip = int(input())
  arr[vip] = 1
count = 0
res = 1
for i in range(1, len(arr)):
  if arr[i] == 0:
    count += 1
  if arr[i] != 0:
    if count != 0:
      res = res * dp[count]
      count = 0
if count != 0:
  res = res * dp[count]
print(res)

