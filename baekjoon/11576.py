import sys
input = sys.stdin.readline

a, b = map(int,input().split())
m = int(input())
number = list(map(int,input().split()))
number.reverse()
res = 0
for i in range(len(number)):
  res += number[i] * pow(a, i)

ans = []

while res > 0:
  tmp = divmod(res, b)
  ans = [tmp[1]] + ans
  res = tmp[0]
  if res < b:
    break
print(res, end=" ")
print(*ans)
