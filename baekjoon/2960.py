import sys
input = sys.stdin.readline

n, k = map(int,input().split())
removed = []
for i in range(2, n+1):
  if len(removed) == k:
    break
  if i not in removed:
    for j in range(i, n+1, i):
      if j not in removed:
        removed.append(j)

print(removed[k-1])
