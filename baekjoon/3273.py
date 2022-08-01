import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
inp = list(map(int,input().split()))
x = int(input())
inp.sort()
left, right = 0, n-1
res = 0
while left < right:
  if inp[left] + inp[right] == x:
    res += 1
    left += 1
    right -= 1
  elif inp[left] + inp[right] > x:
    right -= 1
  else:
    left += 1

print(res)
