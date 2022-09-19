from itertools import permutations
def solution(numbers):
    ans = set([])
    tmp = []
    for n in numbers:
        tmp.append(n)
    tmp = sorted(tmp, reverse = True)
    max_num = int("".join(tmp))
    is_prime = [True for _ in range(max_num+1)]
    is_prime[0], is_prime[1] = False, False
    for i in range(2, max_num+1):
        if is_prime[i]:
            for j in range(i*2, max_num+1, i):
                is_prime[j] = False
                
    for i in range(1, len(numbers)+1):            
        for j in permutations(tmp,i):
            if is_prime[int("".join(j))]:
                ans.add(int("".join(j)))
        
    return len(ans)
