import sys
import math
input = sys.stdin.readline

a = tuple(map(int,input().split()))
b = tuple(map(int,input().split()))

res = [a[0]*b[1] + a[1]*b[0], a[1]*b[1]]
gcd = math.gcd(res[0], res[1])
res[0], res[1] = res[0] // gcd, res[1] // gcd
print("{} {}".format(res[0], res[1]))
