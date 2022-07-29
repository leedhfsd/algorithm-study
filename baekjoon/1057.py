import sys
input = sys.stdin.readline

total, a, b = map(int,input().split())
res = 0

while a != b:
  a -= a // 2
  b -= b // 2
  res += 1

print(res)
