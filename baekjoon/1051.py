import sys
input = sys.stdin.readline

n, m = map(int,input().split())
board = [list(map(int,input().rstrip())) for _ in range(n)]
ans = -sys.maxsize
for i in range(n):
  for j in range(m):
    for k in range(m):
      if j+k >= m or i+k >=n: continue
      if board[i][j] == board[i][j+k] == board[i+k][j] == board[i+k][j+k]:
        cnt = k+1
        if ans < cnt:
          ans = cnt

print(ans * ans)
