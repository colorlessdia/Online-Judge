import sys

while True:
    line = sys.stdin.readline().rstrip()

    if line == '':
        break
    
    s, t = line.split()

    length = len(s)
    i = 0
    temp = ''

    for c in t:
        
        if length <= i:
            break
        
        if temp == s:
            break
        
        if c != s[i]:
            continue
        
        temp += c
        i += 1

    if temp == s:
        print('Yes')
    else:
        print('No')