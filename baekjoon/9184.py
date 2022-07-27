import sys
input = sys.stdin.readline

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def solution(a,b,c):
  if a <= 0 or b <= 0 or c <= 0:
    return 1
  if a > 20 or b > 20 or c > 20:
    return solution(20, 20, 20)
  if dp[a][b][c]:
    return dp[a][b][c]
  elif a < b and b < c:
    dp[a][b][c] = solution(a, b, c-1) + solution(a, b-1, c-1) - solution(a, b-1, c)
  else:
    dp[a][b][c] = solution(a-1, b, c) + solution(a-1, b-1, c) + solution(a-1, b, c-1) - solution(a-1, b-1, c-1)
  
  return dp[a][b][c]
while True:
  a, b, c = map(int,input().split())
  if a == b == c == -1: break

  print("w({}, {}, {}) = {}".format(a,b,c,solution(a, b, c)))
