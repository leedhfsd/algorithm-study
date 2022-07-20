import sys
input = sys.stdin.readline

n = int(input())
res = 0

for i in range(1, n+1):
  if i < 100: res = res + 1
  elif i <= 1000:
    arr = list(str(i))
    arr = list(map(int, arr))
    if arr[0] - arr[1] == arr[1] - arr[2]:
      res = res +1
print(res)
