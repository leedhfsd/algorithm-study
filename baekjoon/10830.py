import sys
input = sys.stdin.readline

n, pow = map(int,input().split())
matrix = []
for _ in range(n):
  matrix.append(list(map(int,input().split())))

def matrix_mul(a, b):
  res = [[0 for _ in range(n)] for _ in range(n)]
  for k in range(n):
    for i in range(n):
      for j in range(n):
        res[k][i] += a[k][j] * b[j][i]

  for i in range(n):
    for j in range(n):
      res[i][j] = res[i][j] % 1000
  return res

def divide(n):
  if n == 1:
    return matrix
  else:
    x = divide(n//2)
    if n % 2 == 0:
      return matrix_mul(x, x)
    else:
      tmp = matrix_mul(x, x)
      return matrix_mul(tmp, matrix)

ans = divide(pow)
for i in range(n):
  for j in range(n):
    print(ans[i][j] % 1000, end=" ")
  print()
