import sys
input = sys.stdin.readline

n = int(input())
book = {}
for _ in range(n):
  inp = input().rstrip()
  if not inp in book:
    book[inp] = 1
  else:
    book[inp] += 1
res = []
for k, v in book.items():
  if v == max(book.values()):
    res.append(k)
res.sort()
print(res[0])
