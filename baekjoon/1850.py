import sys
input = sys.stdin.readline

a, b = map(int,input().split())
while b != 0:
  r = a % b
  a = b
  b = r

print("1"*a)
