import sys
input = sys.stdin.readline

k = int(input())
a = [0 for _ in range(46)]
b = [0 for _ in range(46)]
a[0], a[2] = 1, 1
b[1], b[2] = 1, 1

if k >= 3:
  for i in range(3, k+1):
    a[i] = a[i-2] + a[i-1]
    b[i] = b[i-2] + b[i-1]

print(a[k], b[k])
