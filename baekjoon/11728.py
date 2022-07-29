import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr_n = list(map(int,input().split()))
arr_m = list(map(int,input().split()))

arr = arr_n + arr_m
arr.sort()
print(*arr)


###
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

idx_a, idx_b = 0, 0
ans = []

while idx_a != len(a) and idx_b != len(b):
  if a[idx_a] <= b[idx_b]:
    ans.append(a[idx_a])
    idx_a += 1
  else:
    ans.append(b[idx_b])
    idx_b += 1

if idx_a == len(a):
  ans = ans + b[idx_b:]
else:
  ans = ans + a[idx_a:]

print(*ans)
