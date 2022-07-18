import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]

#for 문 범위 정하는게 중요함
for i in range(n):
  for j in range(i):
    if arr[i] > arr[j]:
      dp[i] = max(dp[j]+1, dp[i])

print(max(dp))
