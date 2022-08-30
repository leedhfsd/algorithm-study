from collections import defaultdict
n = int(input())
fav = defaultdict(list)
order = []
board = [[0 for _ in range(n)] for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def choose(num):
  fav_num = fav[num]
  idx = 0
  count = dict()
  for i in range(n):
    for j in range(n):
      if board[i][j] == 0:
        cnt = 0
        zero = 0
        for k in range(4):
          nx = i + dx[k]
          ny = j + dy[k]

          if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] in fav_num:
              cnt += 1
            elif board[nx][ny] == 0:
              zero += 1
        count[idx] = (cnt, zero)
        idx += 1
      else:
        idx += 1
  tmp = sorted(count.items(), key = lambda x: (-x[1][0],-x[1][1], x[0]))
  det = tmp[0][0]
  row = det // n
  col = det % n
  board[row][col] = num
    
def score():
  res = 0
  for i in range(n):
    for j in range(n):
      cnt = 0
      for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
  
        if 0 <= nx < n and 0 <= ny < n:
          if board[nx][ny] in fav[board[i][j]]:
            cnt += 1
      if cnt > 0:
        res += pow(10, cnt-1)
  return res
    
for i in range(n*n):
  tmp = list(map(int,input().split()))
  fav[tmp[0]] = tmp[1:]
  order.append(tmp[0])

for i in range(len(order)):
  choose(order[i])

print(score())
