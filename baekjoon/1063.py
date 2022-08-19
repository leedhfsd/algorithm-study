import sys
input = sys.stdin.readline

move = {}
move["R"] = (1,0)
move["L"] = (-1,0)
move["B"] = (0,-1)
move["T"] = (0,1)
move["RT"] = (1,1)
move["LT"] = (-1,1)
move["RB"] = (1,-1)
move["LB"] = (-1,-1)

k, r, op = input().split()
king_r, king_c = ord(k[0])-ord("A")+1, int(k[1])
rock_r, rock_c = ord(r[0])-ord("A")+1, int(r[1])

#r 은 가로로 움직임 c는 높이
for _ in range(int(op)):
  move_r, move_c = move[input().rstrip()]
  #만약 킹을 움직였는데 돌의 위치인 경우
  if king_r + move_r == rock_r and king_c + move_c == rock_c:
    tmp_r, tmp_c = rock_r + move_r, rock_c + move_c
    #돌의 위치가 체스판을 벗어나지 않으면 업데이트
    if 1 <= tmp_r <= 8 and 1 <= tmp_c <= 8:
      king_r, king_c = rock_r, rock_c
      rock_r, rock_c = tmp_r, tmp_c
  #킹을 움직여도 돌의 위치가 아닌경우
  elif king_r + move_r != rock_r or king_c + move_c != rock_c:
    tmp_r, tmp_c = king_r + move_r, king_c + move_c
    if 1 <= tmp_r <= 8 and 1 <= tmp_c <= 8:
      king_r, king_c = tmp_r, tmp_c

king = chr(king_r-1+ord("A")) + str(king_c)
rock = chr(rock_r-1+ord("A")) + str(rock_c)

print(king)
print(rock)
