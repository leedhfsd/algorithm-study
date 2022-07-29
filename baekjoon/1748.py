import sys
input = sys.stdin.readline

n = int(input())
length = len(str(n))
ans = (n - pow(10, length-1) + 1)*length
for i in range(1, length):
  ans += 9 * pow(10, i-1) * i

print(ans)
