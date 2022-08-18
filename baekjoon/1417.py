import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
vote = []
for i in range(1,n+1):
  vote.append(int(input()))

flag = False
res = 0
vote.reverse()

while not flag:
  max_vote = max(vote)
  idx = vote.index(max_vote)

  if idx != n-1:
    vote[idx] = vote[idx] - 1
    vote[n-1] = vote[n-1] + 1
    res += 1
  elif idx == n-1:
     flag = True

print(res)
