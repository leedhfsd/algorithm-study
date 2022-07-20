import sys
import math
input = sys.stdin.readline

not_self = []

for i in range(1, 10001):
  arr  = list(str(i))
  res = i
  for j in arr:
    res += int(j)
  not_self.append(res)

for i in range(1, 10001):
  if i not in not_self:
    print(i)
