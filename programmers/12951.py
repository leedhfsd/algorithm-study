def solution(s):
    ans = ""
    for i in range(0,len(s)):
        if i == 0:
            ans += s[i].upper()
        else:
            if s[i-1] == " ":
                ans += s[i].upper()
            else:
                ans += s[i].lower()
    return ans
