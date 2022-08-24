from collections import deque
col, row = map(int,input().split())
n, m = map(int,input().split())
robot = deque([])
op = deque([])
for _ in range(n):
  x, y, dir = input().rstrip().split()
  if dir == "N":
    dir = 0
  elif dir == "E":
    dir = 1
  elif dir == "S":
    dir = 2
  elif dir == "W":
    dir = 3
  robot.append([int(x),int(y),dir])

for _ in range(m):
  number, oper, rep = input().rstrip().split()
  op.append([int(number), oper, int(rep)])

move = [(0,1),(1,0),(0,-1),(-1,0)]
flag = False
crash_robot = -1
while op and not flag:
  number, oper, rep = op.popleft()
  x, y, d = robot[number-1]

  for _ in range(rep):
    if flag: break
    if oper == "L":
      d = (d-1) % 4
    elif oper == "R":
      d = (d+1) % 4
    elif oper == "F":
      nx = x + move[d][0]
      ny = y + move[d][1]
  
      if 1 <= nx <= col and 1 <= ny <= row:
        for i in range(len(robot)):
          if robot[i][0] == nx and robot[i][1] == ny:
            crash_robot = i + 1
            print("Robot {} crashes into robot {}".format(number,crash_robot))
            flag = True
            break
        if not flag:   
          x, y, d = nx, ny, d
      else:
        print("Robot {} crashes into the wall".format(number))
        flag = True
        break
  
  robot[number-1] = [x,y,d]

if not flag:
  print("OK")
