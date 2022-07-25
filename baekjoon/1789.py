import sys
input = sys.stdin.readline

n = int(input())
start = 1

while start*(start+1)/2 <= n:
  if (start+1)*(start+2)/2 > n:
    print(start)
    break
  start = start + 1
