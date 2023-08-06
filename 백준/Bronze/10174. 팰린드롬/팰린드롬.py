import sys

for _ in range(int(input())):
    s = sys.stdin.readline()[:-1].lower()
    
    if len(s) % 2 == 0:
        if (s[: len(s) // 2]) == (s[(len(s) // 2) :][::-1]):
            print('Yes')
        else:
            print('No')
    else:
        if (s[: len(s) // 2]) == (s[(len(s) // 2) + 1 :][::-1]):
            print('Yes')
        else:
            print('No')