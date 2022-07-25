from math import perm
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
arr = [i for i in range(1,n+1)]
res = list(permutations(arr, n))

for item in res:
  for i in item:
    print(i, end=" ")
  print()
