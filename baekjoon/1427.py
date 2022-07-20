import sys
input = sys.stdin.readline

n = list(input().rstrip())
n = list(map(str, n))
n = sorted(n,reverse=True)
print("".join(n))
