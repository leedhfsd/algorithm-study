def solution(n, lost, reserve):
    answer = 0
    inter = set(lost) & set(reserve)
    lost = list(set(lost) - inter)
    reserve = list(set(reserve) - inter)
    used = set([])
    solve = set([])
    for l in lost:
        for r in reserve:
            if r not in used:
                if l == r-1 or l == r+1:
                    used.add(r)
                    solve.add(l)
                    break

    answer = n - len(lost) + len(solve)
    return answer
