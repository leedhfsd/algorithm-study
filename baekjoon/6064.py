#중국인의 나머지정리? 잘 모르겠고 그냥 최적화
import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
  m, n, x, y = map(int,input().split())
  cur = x
  while True:
    if (cur-x) % m == 0 and (cur-y) % n == 0:
      print(cur)
      break
    else:
      cur += m
    if cur > m * n:
      print(-1)
      break
