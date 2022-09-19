answer = 0
def recursion(cur,n,res,target,arr):
    global answer
    if cur >= n:
        if res == target:
            answer += 1
        else:
            return 0
    else:
        recursion(cur+1, n, res+arr[cur], target, arr)
        recursion(cur+1, n, res-arr[cur], target, arr)

            
def solution(numbers, target):
    global answer
    recursion(0,len(numbers),0,target, numbers)
    return answer
