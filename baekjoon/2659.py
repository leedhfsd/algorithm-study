n = input().split()

def small(arr):
  tmp_0 = int("".join(arr))
  tmp_1 = int("".join(arr[1:] + [arr[0]]))
  tmp_2 = int("".join(arr[2:] + arr[:2]))
  tmp_3 = int("".join([arr[3]] + arr[0:3]))
  
  return min(tmp_0, tmp_1, tmp_2, tmp_3)

n = small(n)
ans = 0

for i in range(1111, 10000):
  tmp = small(list(str(i)))
  if  "0" in str(i) or tmp < i: continue
  else:
    ans += 1
    if n == i:
      print(ans)
      break
