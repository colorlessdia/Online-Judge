S = input()

condition_1 = True if 2 <= len(S) else False
condition_2 = True if S[0] == S[-1] == '"' else False
condition_3 = True if 0 < len(S[1:-1]) else False

if condition_1 and condition_2 and condition_3:
    print(S[1:-1])
else:
    print('CE')