import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = set(map(int,input().split()))
b = set(map(int,input().split()))
res = 0
for i in a:
  if i in b:
    res += 1

print(len(a) - res + len(b) - res)
