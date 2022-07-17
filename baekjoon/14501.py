import sys
input = sys.stdin.readline
n = int(input())
sche = [list(map(int,input().split())) for _ in range(n)]

def recursion(day, cur):
  res = 0
  if day > n:
    return 0
  if day == n:
    return cur

  days, pay = sche[day]
  res = max(recursion(day+days, cur+pay), recursion(day+1, cur))

  return res

print(recursion(0,0))
