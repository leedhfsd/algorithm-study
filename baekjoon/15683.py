import sys
import copy
input = sys.stdin.readline

row, col = map(int,input().split())
area = [list(map(int,input().split())) for _ in range(row)]
r = [(-1,0),(0,1),(1,0),(0,-1)]
cam_1 = [[r[0]], [r[1]], [r[2]], [r[3]]]
cam_2 = [[r[0], r[2]], [r[1], r[3]]]
cam_3 = [[r[0],r[1]], [r[1], r[2]], [r[2], r[3]], [r[3], r[0]]]
cam_4 = [[r[0],r[1],r[2]], [r[1],r[2],r[3]], [r[2],r[3],r[0]], [r[3],r[0],r[1]]]
cam_5 = [[r[0], r[1], r[2], r[3]]]
direction = [cam_1, cam_2, cam_3, cam_4, cam_5]
ans = sys.maxsize
def count(arr):
	cnt = 0
	for i in range(row):
		for j in range(col):
			if arr[i][j] == 0:
				cnt += 1
	return cnt

def draw(x, y, arr, cam, num):
	move = direction[cam][num]
	
	for dx, dy in move:
		nx = x + dx
		ny = y + dy
		
		while 0 <= nx < row and 0 <= ny < col:
			if arr[nx][ny] == 6:
				break
			else:
				if arr[nx][ny] in [1,2,3,4,5,"#"]:
					nx = nx + dx
					ny = ny + dy
				elif arr[nx][ny] == 0:
					arr[nx][ny] = "#"
					nx = nx + dx
					ny = ny + dy
	
#처음에 카메라 위치를 전부 받아서 리스트에 저장
camera = []
for i in range(row):
	for j in range(col):
		if area[i][j] in [1,2,3,4,5]:
			camera.append((i, j, area[i][j]))

def recursion(arr, res):
	global ans
	if res == len(camera):
		zero = count(arr)
		if ans > zero:
			ans = zero
		return 0

	x, y, number = camera[res]
	tmp = copy.deepcopy(arr)
	for i in range(len(direction[number-1])):
		draw(x, y, tmp, number-1, i)
		recursion(tmp, res+1)
		tmp = copy.deepcopy(arr)

recursion(area, 0)
print(ans)
