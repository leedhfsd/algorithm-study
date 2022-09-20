# 재귀로 구현시 recursion 오류남

from collections import deque
def solution(queue1, queue2):
    answer = 0
    sum1, sum2 = sum(queue1), sum(queue2)
    dq1, dq2 = deque(queue1), deque(queue2)
    score = sum1 + sum2
    
    if score % 2 != 0:
        return -1
    
    while True:
        if answer > (len(queue1) + len(queue2)) * 2:
            return -1
        
        if sum1 == sum2:
            return answer
        elif sum1 > sum2:
            tmp = dq1.popleft()
            dq2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
        else:
            tmp = dq2.popleft()
            dq1.append(tmp)
            sum2 -= tmp
            sum1 += tmp
        answer += 1
    
