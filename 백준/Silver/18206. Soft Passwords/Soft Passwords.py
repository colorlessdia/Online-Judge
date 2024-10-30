S = input()
P = input()

condition_1 = S == P
condition_2 = S[1:] == P and S[0].isdigit()
condition_3 = S[:-1] == P and S[-1].isdigit()
condition_4 = S == ''.join([p.upper() if p.islower() else p.lower() for p in P])

if any([condition_1, condition_2, condition_3, condition_4]):
    print('Yes')
else:
    print('No')