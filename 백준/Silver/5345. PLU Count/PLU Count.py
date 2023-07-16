import sys

for _ in range(int(input())):
    s = sys.stdin.readline().rstrip().lower()
    cnt = 0
    chk = ''
    
    for c in s:
        if len(chk) == 0 and c == 'p':
            chk += c
        elif len(chk) == 1 and c == 'l':
            chk += c
        elif len(chk) == 2 and c == 'u':
            chk += c
            cnt += 1
            chk = ''
            
    print(cnt)