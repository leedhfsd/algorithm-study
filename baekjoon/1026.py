import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(2)]

arr[0].sort(reverse=True)
arr[1].sort()
res = 0
for i in range(n):
  res += arr[0][i] * arr[1][i]

print(res)
