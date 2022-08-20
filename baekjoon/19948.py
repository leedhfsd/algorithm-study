poem = input().upper().split()
space = int(input())
alpha = list(map(int,input().split()))

if len(poem) > space + 1:
  print(-1)
else:
  flag = False
  prev = ""
  for i in range(len(poem)):
    tmp = poem[i]
    for j in range(len(tmp)):
      alpha[ord(tmp[j])-ord("A")] -= 1
      if tmp[j] == prev:
        alpha[ord(tmp[j])-ord("A")] += 1
      prev = tmp[j]
      if alpha[ord(tmp[j])-ord("A")] < 0:
        flag = True
        break
  res = ""
  if flag:
    print(-1)
  else:
    for i in range(len(poem)):
      tmp = poem[i][0]
      if alpha[ord(tmp)-ord("A")] > 0:
        res = res + tmp
      else:
        res = -1
        break
    print(res)
