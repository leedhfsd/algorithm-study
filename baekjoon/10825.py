import sys
input = sys.stdin.readline

n = int(input())
inp = [list(input().split()) for _ in range(n)]
inp.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for item in inp:
  print(item[0])
