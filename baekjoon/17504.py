from math import gcd
import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int,input().split()))

top, bottom = 1, number[n-1]
res = 0
for i in range(n-1, 0, -1):
  a, b = [top, bottom], number[i-1]
  top, bottom = top + b * bottom, bottom
  gc = gcd(top,bottom)
  top, bottom = bottom // gc, top // gc

print(bottom - top, bottom)
