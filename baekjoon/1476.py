import sys
input = sys.stdin.readline

e, s, m = map(int,input().split())

year = 1
e_pos, s_pos, m_pos = 0, 0, 0
while True:
  if year % 15 == 0:
    e_pos = 15
  else:
    e_pos = year % 15
  
  if year % 28 == 0:
    s_pos = 28
  else:
    s_pos = year % 28

  if year % 19 == 0:
    m_pos = 19
  else:
    m_pos = year % 19

  if e_pos == e and s_pos == s and m_pos == m:
    print(year)
    break
  else:
    year = year + 1
  
