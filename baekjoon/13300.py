import math
n, k = map(int,input().split())
student = [[0 for _ in range(6)] for _ in range(2)]
for _ in range(n):
  sex, grade = map(int,input().split())
  student[sex][grade-1] += 1
ans = 0

for i in range(2):
  for j in range(6):
    ans += math.ceil(student[i][j] / k)

print(ans)
