import sys
import math
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  west, east = map(int,input().split())
  print(math.comb(east,west))
