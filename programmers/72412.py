# bisect_left는 이진 탐색에서 들어갈 인덱스의 가장 왼쪽을 찾을 때 사용
# 문제의 컨셉 => 경우의 수가 전부 많은데 어떻게 해결할 것 인가? => 모든 케이스에 대해 dict에 저장해놓고 기록해놓기

from collections import defaultdict
from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    for inf in info:
        lis = inf.split()
        tmp = lis[0:4]
        for i in range(5):
            for j in combinations(tmp, i):
                key = "".join(j)
                info_dict[key].append(int(lis[4]))
    
    for keys in info_dict.keys():
        info_dict[keys].sort()
    
    for q in query:
        tmp = q.split()
        tmp = [i for i in tmp if i != "and"]
        keys = "".join(tmp[0:4]).replace("-","")
        if info_dict[keys]:
            answer.append(len(info_dict[keys]) - bisect_left(info_dict[keys], int(tmp[4])))
        else:
            answer.append(0)
    return answer
