def solution(N, stages):
    answer = []
    eqaul, over = 0, 0
    for i in range(1,N+1):
        equal = 0
        over = 0
        for j in stages:
            if j > i:
                over += 1
            elif j == i:
                equal += 1
        if over + equal == 0:
            answer.append((i, 0))
        else:
            answer.append((i, equal/(over+equal)))
    answer.sort(key = lambda x: (-x[1],x[0]))
    ans = []
    for i in range(len(answer)):
         ans.append(answer[i][0])               
    return ans
