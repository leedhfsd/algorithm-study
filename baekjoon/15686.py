import sys
input = sys.stdin.readline

n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

home, chick = [], []
for i in range(n):
  for j in range(n):
    if board[i][j] == 1:
      home.append((i,j))
    elif board[i][j] == 2:
      chick.append((i,j))
candidate = set([])
ans = sys.maxsize

def choose(res, idx):
  global ans, candidate

  if res == m:
    tmp = 0
    for i in range(len(home)):
      x1, y1 = home[i]
      cnt = sys.maxsize
      for j in candidate:
        x2, y2 = j
        dis = abs(x1-x2) + abs(y1-y2)
        if dis < cnt:
          cnt = dis
      tmp += cnt
    if tmp < ans:
      ans = tmp
    return 0

  for i in range(idx, len(chick)):
    candidate.add(chick[i])
    choose(res+1, i+1)
    candidate.remove(chick[i])

choose(0, 0)
print(ans)
