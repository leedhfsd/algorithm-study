def solution(brown, yellow):
    answer = []
    c = brown + yellow
    ans = []
    flag = False
    for i in range(1, c+1):
        if flag:
            break
        if c % i != 0: continue
        if not flag:
            for j in range(1, yellow+1):
                if (i-2) * j == yellow and i * 2 + j * 2 == brown:
                    flag = True
                    ans = [c//i , i]
                    break                   
    return ans
