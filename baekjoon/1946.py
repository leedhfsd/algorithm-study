#왼쪽 기준으로 정렬할필요가 있는 문제이다.
#sort를 쓰면 간단하게 정렬이 되지만 왼쪽 점수를 index로 하는 배열을 하나 만들면 sort를 하지 않아도 동일한 효과 가능

import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
  n = int(input())
  score = [0 for _ in range(n+1)]
  for _ in range(n):
    a, b = map(int,input().split())
    score[a] = b

  std = score[1]
  res = 1
  for i in range(2, n+1):
    if score[i] < std:
      res += 1
      std = score[i]
  
  print(res)
      
