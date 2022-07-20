import sys
input = sys.stdin.readline

n = int(input())
res = 0

for _ in range(n):
  word = input().rstrip()
  used = []
  cur = ""
  flag = True
  for i in word:
    if i not in used:
      used.append(cur)
      cur = i
    else:
      if cur != i:
        flag = False
        break
  if flag:
    res += 1
print(res)
