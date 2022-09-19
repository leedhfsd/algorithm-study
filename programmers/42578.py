from collections import defaultdict
def solution(clothes):
    answer = 1
    cloth = defaultdict(list)
    tmp = []
    for i in clothes:
        a, b = i
        cloth[b].append(a)
    for v in cloth.values():
        tmp.append(len(v))
    for num in tmp:
        answer *= (1+num)
    return answer - 1
