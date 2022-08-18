import sys
input = sys.stdin.readline

n, b, h, w = map(int,input().split())
hotel = []
res = sys.maxsize
flag = False
for i in range(h):
  cost = int(input())
  count = map(int,input().split())
  max_client = max(count)
  if max_client < n:
    continue
  else:
    tmp = n * cost
    if tmp < res and tmp <= b:
      res = tmp
      flag = True

if flag:
  print(res)
else:
  print("stay home")
