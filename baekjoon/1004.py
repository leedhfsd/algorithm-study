import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
  x1,y1,x2,y2 = map(int,input().split())
  n = int(input())
  inp = []
  for i in range(n):
    inp.append(list(map(int,input().split())))
  #inp에서 하나씩 시작 끝 지점속한 원 개수 세기
  res = 0
  for j in range(n):
    x, y, r = inp[j]
    tmp_1 = pow((x1-x), 2) + pow((y1-y), 2)
    tmp_2 = pow((x2-x), 2) + pow((y2-y), 2)

    if r*r >= tmp_1 and not r*r >= tmp_2:
      res += 1
    elif not r*r >= tmp_1 and r*r >= tmp_2:
      res += 1
  
  print(res)
