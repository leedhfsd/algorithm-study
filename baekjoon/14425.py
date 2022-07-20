import sys
input = sys.stdin.readline

n, m = map(int, input().split())
word = set()
count = 0
for i in range(n):
  word.add(input().rstrip())

for _ in range(m):
  inp = input().rstrip()
  if inp in word:
    count += 1

print(count)
