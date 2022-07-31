import sys
input = sys.stdin.readline

n = int(input())
inp = list(set(list(map(int,input().split()))))
inp.sort()
print(*inp)
