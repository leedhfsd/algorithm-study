import sys
input = sys.stdin.readline

inp = input().rstrip()
flag = True
ans = ""
tmp = ""
idx = 0

while True:
  if idx == len(inp):
    break
  
  if inp[idx] == "<":
    ans += tmp
    tmp = ""
    while inp[idx] != ">":
      ans += inp[idx]
      idx += 1
    ans += ">"
    idx += 1
  else:
    if inp[idx] == " ":
      ans += tmp + " "
      tmp = ""
      idx += 1
    else:  
      tmp = inp[idx] + tmp
      idx += 1

print(ans+tmp)
