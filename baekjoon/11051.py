import sys
import math
input = sys.stdin.readline

n, k = map(int, input().split())
print(math.comb(n, k) % 10007)
