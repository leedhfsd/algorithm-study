import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = []
dp = deque([[[0,0] for _ in range(3)] for _ in range(2)])

max_ans, min_ans = -sys.maxsize, sys.maxsize
for i in range(1, n+1):
  board = list(map(int,input().split()))
  dp[1][0][0] = max(dp[0][0][0], dp[0][1][0]) + board[0]
  dp[1][0][1] = min(dp[0][0][1], dp[0][1][1]) + board[0]
  dp[1][1][0] = max(dp[0][0][0], dp[0][1][0], dp[0][2][0]) + board[1]
  dp[1][1][1] = min(dp[0][0][1], dp[0][1][1], dp[0][2][1]) + board[1]
  dp[1][2][0] = max(dp[0][1][0], dp[0][2][0]) + board[2]
  dp[1][2][1] = min(dp[0][1][1], dp[0][2][1]) + board[2]
  dp.popleft()
  dp.append([[0,0],[0,0],[0,0]])

for i in dp[0]:
  a, b = i
  if a > max_ans:
    max_ans = a
  if b < min_ans:
    min_ans = b

print(max_ans, min_ans)
