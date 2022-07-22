import sys
input = sys.stdin.readline

n = int(input())
n_num = set(list(map(int,input().split())))
m = int(input())
m_num = list(map(int,input().split()))

for num in m_num:
  if num in n_num:
    print("1",end=" ")
  else:
    print("0",end=" ")
