#문자열 비교는 각 자리수의 아스키코드값이 크면 크다고 판정
#"30300" < "333" 은 참이다.
#람다식 사용할때 x에 변화를 줄 수 있음. x*4는 문자열 x를 4번 반복한 것이다.

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*4, reverse = True)
    answer = str(int("".join(numbers)))
    return answer
