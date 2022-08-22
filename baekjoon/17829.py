n = int(input())
inp = [list(map(int,input().split())) for _ in range(n)]

ans = 0
def divide(board, n):
  global ans
  if n == 2:
    tmp = []
    for i in range(2):
      for j in range(2):
        tmp.append(board[i][j])
    ans = sorted(tmp)[2]
    return 0

  half = [[0 for _ in range(n//2)] for _ in range(n//2)]
  cand = []
  for i in range(n):
    if i % 2 != 0: continue
    for j in range(n):
      if j % 2 != 0: continue
      tmp = sorted([board[i][j], board[i][j+1],board[i+1][j],board[i+1][j+1]])[2]
      cand.append(tmp)
  
  if len(cand) == 4:
    ans = sorted(cand)[2]
    return 0
  
  idx = 0
  for i in range(n//2):
    for j in range(n//2):
      half[i][j] = cand[idx]
      idx += 1
  divide(half, n//2)


divide(inp, n)
print(ans)
