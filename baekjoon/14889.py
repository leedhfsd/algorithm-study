#조합말고 백트래킹으로 어떻게 풂??
import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
people = [i for i in range(n)]
ans = sys.maxsize

comb = combinations(people, n//2)

for i in comb:
  res1, res2 = 0, 0
  team2 = list(set(people) - set(i))
  team1 = list(i)

  for j in combinations(team1,2):
    x, y = j
    res1 += board[x][y] + board[y][x]
  
  for j in combinations(team2,2):
    x, y = j
    res2 += board[x][y] + board[y][x]
  
  ans = min(ans, abs(res1-res2))
print(ans)  
