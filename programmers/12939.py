def solution(s):
    answer = ''
    num = list(map(int,s.split()))
    ans = [min(num),max(num)]
    answer = "{} {}".format(ans[0],ans[1])
    return answer
