import sys
input = sys.stdin.readline

total, win = map(int,input().split())
rate = win * 100 / total
left, right = 1 , total
ans = 0
if rate >= 99:
  print(-1)
else:
  while left <= right:
    mid = (left + right) // 2
    if rate < (win + mid) * 100 // (total + mid):
      ans = mid
      right = mid -1
    else:
      left = mid + 1
  print(ans)
