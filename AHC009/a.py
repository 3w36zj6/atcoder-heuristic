from decimal import Decimal

S_I, S_J, T_I, T_J, P = input().split()
S_I, S_J, T_I, T_J = map(int,(S_I, S_J, T_I, T_J))
P = Decimal(P)
H = [list(map(bool,list(input()))) for _ in range(20)]
V = [list(map(bool,list(input()))) for _ in range(19)]

