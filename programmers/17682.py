def solution(dartResult):
    tmp = ""
    idx = 0
    res = 0
    used = []
    while idx < len(dartResult):
        if dartResult[idx] in "0123456789":
            tmp += dartResult[idx]
            if dartResult[idx+1] in "0123456789":
                tmp += dartResult[idx+1]
                idx += 1
        elif dartResult[idx] in "SDT":
            if dartResult[idx] == "S":
                res += int(tmp)
                used.append(int(tmp))
                tmp = ""
            elif dartResult[idx] == "D":
                res += pow(int(tmp),2)
                used.append(pow(int(tmp),2))
                tmp = ""
            elif dartResult[idx] == "T":
                res += pow(int(tmp),3)
                used.append(pow(int(tmp),3))
                tmp = ""
                
        elif dartResult[idx] in "*#":
            if dartResult[idx] == "*":
                if len(used) == 1: 
                    res += used[-1]
                    used[-1] = used[-1] * 2
                elif len(used) > 1:
                    res += used[-1] + used[-2]
                    used[-1], used[-2] = used[-1] * 2, used[-2] * 2
            elif dartResult[idx] == "#":
                used[-1] = -used[-1]
                res += used[-1] * 2
        idx += 1
        
    return res
