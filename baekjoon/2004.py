#n!에서 2와 5의 개수를 세는 문제, 2의 개수를 세는 방법은 n까지 2의 배수 개수는 n // 2, 여기서 한번 더 하면 4의 배수 개수..

import sys
input = sys.stdin.readline

a, b = map(int,input().split())

def check_two(number):
  two_count = 0
  while number != 0:
    number = number // 2
    two_count += number

  return two_count

def check_five(number):
  five_count = 0
  while number != 0:
    number = number // 5
    five_count += number

  return five_count

print(min((check_two(a) - check_two(b) - check_two(a-b)), (check_five(a) - check_five(b) - check_five(a-b))))
