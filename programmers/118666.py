from collections import defaultdict
def solution(survey, choices):
    answer = ""
    score = defaultdict(list)
    score["R"], score["T"], = 0, 0
    score["C"], score["F"], = 0, 0
    score["J"], score["M"], = 0, 0
    score["A"], score["N"], = 0, 0
    test_score = [0,3,2,1,0,1,2,3]
    
    for i in range(len(survey)):
        tmp = survey[i]
        choice = choices[i]
        first, second = tmp[0], tmp[1]
        if choice <= 3:
            score[first] += test_score[choice]
        elif choice == 4:
            continue
        elif choice > 4:
            score[second] += test_score[choice]
    
    if score["R"] >= score["T"]:
        answer += "R"
    else:
        answer += "T"
        
    if score["C"] >= score["F"]:
        answer += "C"
    else:
        answer += "F"
        
    if score["J"] >= score["M"]:
        answer += "J"
    else:
        answer += "M"
    
    if score["A"] >= score["N"]:
        answer += "A"
    else:
        answer += "N"
        
    return answer
