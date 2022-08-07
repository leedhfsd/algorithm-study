import sys
from math import gcd

input = sys.stdin.readline

n = int(input())
inp = list(map(int,input().split()))

for i in range(1, n):
  num = gcd(inp[0], inp[i])
  print("{}/{}".format(inp[0]//num, inp[i]//num))
