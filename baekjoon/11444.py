n = int(input())
base = [[1,1],[1,0]]

m = 1000000007
def mul_matrix(x, y):
  a00 = (x[0][0] * y[0][0] + x[0][1] * y[1][0]) % m
  a01 = (x[0][0] * y[0][1] + x[0][1] * y[1][1]) % m
  a11 = (x[1][0] * y[0][0] + x[1][1] * y[1][0]) % m
  a12 = (x[1][0] * y[0][1] + x[1][1] * y[1][1]) % m

  return [[a00,a01],[a11,a12]]

def fib(n):
  if n == 1:
    return base 
  else:
    x = fib(n // 2)
    
    if n % 2 == 0:
      return mul_matrix(x, x)
    else:
      tmp = mul_matrix(x, x)
      return mul_matrix(tmp, base)

print(fib(n)[0][1] % m)
