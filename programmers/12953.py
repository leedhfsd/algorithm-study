#유클리드 호제법은 외워놓기
#프로그래머스 컴파일러 버전이 낮아서 import math  math.gcd 사용 불가임
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a*b)//gcd(a,b)

def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])
    return answer
