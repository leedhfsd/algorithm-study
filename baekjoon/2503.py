import sys
input = sys.stdin.readline

tc = int(input())
not_candidate = set([])
for _ in range(tc):
  num, st, ball = map(int,input().split())
  num_lis = list(str(num))
  for i in range(100, 1000):
    tmp = list(str(i))
    if "0" in tmp: 
      not_candidate.add(i)
      continue
    if len(set(tmp)) < 3:
      not_candidate.add(i)
      continue
    
    tmp_st, tmp_ball = 0, 0
    for j in range(3):
      if tmp[j] == num_lis[j]:
        tmp_st += 1
      elif tmp[j] != num_lis[j] and tmp[j] in num_lis:
        tmp_ball += 1
    if tmp_st != st or tmp_ball != ball:
      not_candidate.add(i)
  
print(900-len(not_candidate))  
