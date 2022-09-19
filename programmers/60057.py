def solution(s):
    answer = 10000000
    for i in range(1, len(s)+1):
        char = s[:i]
        res = ""
        cnt = 1
        for j in range(i, len(s)+i, i):
            if char == s[j:j+i]:
                cnt += 1
            else:
                if cnt != 1:
                    res += "{}{}".format(cnt,char)
                else:
                    res += char
                cnt = 1
                char = s[j:j+i]
        if len(res) < answer:
            answer = len(res)
    return answer
