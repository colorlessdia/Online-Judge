import sys

while 1:
    s = sys.stdin.readline().rstrip()
    if s == '#': break

    l = s[-1]
    s = s[:-1]
    diff = ord(l) - ord('A')
    dc = ''
    for ss in s:
        if ss.isalpha() and ss.isupper():
            if ord(ss) - diff < ord('A'):
                dc += chr(ord('Z') - (ord('A') - (ord(ss) - diff)) + 1)
            else:
                dc += chr(ord(ss) - diff)
        elif ss.isalpha() and ss.islower():
            if ord(ss) - diff < ord('a'):
                dc += chr(ord('z') - (ord('a') - (ord(ss) - diff)) + 1)
            else:
                dc += chr(ord(ss) - diff)
        else:
            dc += ss
    
    print(dc)