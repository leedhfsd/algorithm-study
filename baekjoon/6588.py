import sys
input = sys.stdin.readline

ans = ""
is_prime = [1 for _ in range(1000001)]
is_prime[0], is_prime[1] = 0, 0
for i in range(2, 1000001):
  if not is_prime:
    continue
  j = i * i
  for j in range(j, 1000001, i):
    is_prime[j] = 0

while True:
  inp = int(input())
  flag = False
  if inp == 0: break
  for i in range(2, inp):
    if is_prime[i] and is_prime[inp-i]:
      ans += "{} = {} + {}\n".format(inp, i, inp-i)
      flag = True
      break
  if not flag:
    ans += "Goldbach's conjecture is wrong.\n"
print(ans)
