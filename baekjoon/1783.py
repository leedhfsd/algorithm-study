n, m = map(int,input().split())

if n >= 3 and m <= 4:
  print(m)
elif n >= 3 and m <= 6:
  print(4)
elif n >= 3 and m > 6:
  print(m-2)
elif n == 2 and m < 9:
  print((m+1)//2)
elif n == 2 and m >= 9 :
  print(4)
elif n == 1:
  print(1)
