import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a, b = [], []

for _ in range(n):
  a.append(list(map(int, input().rstrip())))
for _ in range(n):
  b.append(list(map(int, input().rstrip())))

def change(x, y):
  global a
  for i in range(x, x+3):
    for j in range(y, y+3):
      if a[i][j] == 0:
        a[i][j] = 1
      else:
        a[i][j] = 0

res = 0
flag = False
for i in range(n):
  for j in range(m):
    if i+2 >= n or j+2 >= m: continue
    if a[i][j] != b[i][j]:
      change(i, j)
      res += 1

for i in range(n):
  if flag:
    break
  for j in range(m):
    if a[i][j] != b[i][j]:
      flag = True
      break
if flag:
  print(-1)
else:
  print(res)
