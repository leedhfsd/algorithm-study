#루트보다 처음 큰 수는 루트의 오른쪽 트리에 존재하는 수이다.
#그 수의 바로 전 인덱스에 있는 수는 왼쪽 트리에 존재하는 마지막 수, start+1은 그 왼쪽트리의 첫번째 수이다
#처음 호출하는 postorder는 루트의 왼쪽 자식을 루트로 하는 트리에서 왼쪽 트리를 찾는 것


import sys
sys.setrecursionlimit(10**9)
tree = []
while True:                            
    try:
        tree.append(int(sys.stdin.readline()))
    except:
        break

def postorder(start, end):
  if start > end:
    return 0

  idx = start+1
  for i in range(start+1, end+1):
    if tree[i] > tree[start]:
      idx = i
      break
  
  postorder(start+1, idx-1)
  postorder(idx, end)
  print(tree[start])

postorder(0, len(tree)-1)
