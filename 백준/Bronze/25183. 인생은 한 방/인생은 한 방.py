n = int(input())
s = input()

before = ' '
cnt = 0
isTrue = False

for c in s:
    mx = max(ord(before), ord(c))
    mn = min(ord(before), ord(c))
    
    if mx - mn == 1:
        cnt += 1
    else:
        cnt = 0

    before = c
    
    if cnt == 4:
        isTrue = True
        break

if isTrue:
    print('YES')
else:
    print('NO')