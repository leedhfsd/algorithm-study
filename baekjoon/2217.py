import sys
input = sys.stdin.readline

n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort()
ans = 0
for i in range(n):
  res = rope[i] * (n-i)
  ans = max(res, ans)

print(ans)
