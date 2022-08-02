import sys
input = sys.stdin.readline

inp = input().rstrip()
word = input().rstrip()
res = 0

while True:
  idx = inp.find(word)
  if idx == -1:
    break
  inp = inp[idx+len(word):]
  res += 1

print(res)
