import sys
input = sys.stdin.readline

n_a, m_a = map(int,input().split())
matrix_A, matrix_B = [], []
for _ in range(n_a):
  matrix_A.append(list(map(int,input().split())))

n_b, m_b = map(int,input().split())
for _ in range(n_b):
  matrix_B.append(list(map(int,input().split())))

res = [[0 for _ in range(m_b)] for _ in range(n_a)]

for i in range(n_a):
  for j in range(m_a):
    for k in range(m_b):
      res[i][k]  += matrix_A[i][j] * matrix_B[j][k] 

for i in range(len(res)):
  print(*res[i])
