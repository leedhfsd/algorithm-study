import sys
from collections import defaultdict
input = sys.stdin.readline

score = defaultdict(int)
for i in range(1,9):
  score[i] = int(input())
res = ""
sorted_score = sorted(score.values())[3:]
for k, v in score.items():
  if v in sorted_score:
    res += str(k)+" "
print(sum(sorted_score))
print(res)
