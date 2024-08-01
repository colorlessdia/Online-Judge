N = int(input())
S = input()

if len(S) <= 25:
    print(S)
else:
    word = S[11:-11]

    if '.' in word:
        
        if '.' in word[:-1]:
            print(S[:9] + '......' + S[-10:])
        else:
            print(S[:11] + '...' + S[-11:])
    else:
        print(S[:11] + '...' + S[-11:])