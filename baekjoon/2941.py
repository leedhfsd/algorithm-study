import sys
input = sys.stdin.readline

word = input().rstrip()
alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in alpha:
  word = word.replace(i, "a")
print(len(word))
