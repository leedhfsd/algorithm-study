import sys
sys.setrecursionlimit(10**6)
n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

idx = [0] * (n+1)
for i in range(n):
  idx[inorder[i]] = i

def preorder(in_start, in_end, post_start, post_end):
  if in_start > in_end or post_start > post_end:
    return 0

  root = postorder[post_end]
  left = idx[root] - in_start
  right = in_end - idx[root]
  print(root, end=" ")

  preorder(in_start, idx[root]-1, post_start, post_start+left-1)
  preorder(idx[root]+1, in_end, post_end-right, post_end-1)

preorder(0,n-1,0,n-1)
