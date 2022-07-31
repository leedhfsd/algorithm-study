import sys
input = sys.stdin.readline

n = int(input())
candy = [list(input().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
ans = -sys.maxsize

def check():
  global candy, ans
  for i in range(n):
    res = 1
    for j in range(1, n):
      if candy[i][j] == candy[i][j-1]:
        res += 1
      else:
        res = 1
      if res > ans:
        ans = res
    res = 1
    for j in range(1, n):
      if candy[j][i] == candy[j-1][i]:
        res += 1
      else:
        res = 1
      if res > ans:
        ans = res

for i in range(n):
  for j in range(n):
    if j < n-1 and candy[i][j] != candy[i][j+1]:
      candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
      check()
      candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
    if i < n-1 and candy[i][j] != candy[i+1][j]:
      candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
      check()
      candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

print(ans)
