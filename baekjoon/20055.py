import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())
belt = deque(list(map(int,input().split())))
robot = deque([False for _ in range(n*2)])
res = 0

while True:
  belt.rotate(1)
  robot.rotate(1)
  robot[n-1] = False   

  for i in range(n*2-2, -1, -1):
    if robot[i] and belt[i+1] >= 1 and not robot[i+1]:
      robot[i], robot[i+1] = False, True
      belt[i+1] -= 1
  robot[n-1] = False

  if belt[0] > 0:
    robot[0] = True
    belt[0] -= 1
  
  res += 1
  if belt.count(0) >= k:
    print(res)
    break
