import sys
input = sys.stdin.readline

op = {}
op["ADD"], op["ADDC"] = "000000", "000010"
op["SUB"], op["SUBC"] = "000100", "000110"
op["MOV"], op["MOVC"] = "001000", "001010"
op["AND"], op["ANDC"] = "001100", "001110"
op["OR"], op["ORC"] = "010000", "010010"
op["NOT"] = "010100"
op["MULT"], op["MULTC"] = "011000", "011010"
op["LSFTL"], op["LSFTLC"] = "011100", "011110"
op["LSFTR"], op["LSFTRC"] = "100000", "100010"
op["ASFTR"], op["ASFTRC"] = "100100", "100110"
op["RL"], op["RLC"] = "101000", "101010"
op["RR"], op["RRC"] = "101100", "101110"

tc = int(input())
for _ in range(tc):
  inp = input().rstrip().split()
  oper = inp[0]
  a = int(inp[1])
  b = int(inp[2])
  c = int(inp[3])
  res = ""
  res = res + op[oper]
  res = res + bin(a)[2:].zfill(3)
  res = res + bin(b)[2:].zfill(3)
  if res[4] == "0":
    res = res + bin(c)[2:].zfill(3) + "0"
  else:
    res = res + bin(c)[2:].zfill(4)

  print(res)
