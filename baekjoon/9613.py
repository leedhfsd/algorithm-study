import sys
from itertools import combinations
import math
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  number = list(map(int,input().split()))
  number.pop(0)
  res = 0
  comb = list(combinations(number, 2))
  for x,y in comb:
    gcd = math.gcd(x, y)
    res += gcd
  
  print(res)
