#110011 을 0을 기준으로 split하면 ["11", "", "11"]이 나온다.

import math
def change(a, b):
    res = ""
    while a >= 1:
        tmp = divmod(a, b)
        res = str(tmp[1]) + res
        a = tmp[0]
    return res

def is_prime(n):
    flag = True
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            flag = False
            break
    return flag

def solution(n, k):
    answer = 0
    if k != 10:
        cand = change(n,k)
    else:
        cand = str(n)

    cand = cand.split("0")
    for num in cand:
        if not num:
            continue
        if is_prime(int(num)):
            answer += 1
    return answer
