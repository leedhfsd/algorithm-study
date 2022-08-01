import sys
input = sys.stdin.readline

n, m = map(int,input().split())
res = 0

package = []
piece = []

for _ in range(m):
  a, b = map(int,input().split())
  package.append(a)
  piece.append(b)

package.sort()
piece.sort()

quotient, remainder = divmod(n, 6)

if n <= 6:
  res = min(package[0], piece[0]*n)
else:
  res = min(package[0] * (quotient+1), package[0] * quotient + piece[0] * remainder, piece[0] * n)

print(res)
