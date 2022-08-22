n = int(input())
m = int(input())
frame = [[-1,-1,-1] for _ in range(n)]
number = list(map(int,input().split()))

for i in range(m):
  #frame
  flag = False
  for j in range(n):
    #이미 같은 게 존재하는 경우
    if number[i] == frame[j][1]:
      flag = True
      frame[j][0] += 1
      break
    #존재하지 않은 경우 빈 프레임이 있으면 그곳에 아니면 횟수가 가장 작은 곳으로
  if not flag:
    if [-1,-1,-1] in frame:
      frame[frame.index([-1,-1,-1])] = [1, number[i], i]
    else:
      frame.sort(key = lambda x: (x[0], x[2]))
      frame[0] = [1, number[i], i]

tmp = []
for i in range(n):
  if frame[i][1] != -1:
    tmp.append(frame[i][1])
tmp.sort()
print(*tmp)
