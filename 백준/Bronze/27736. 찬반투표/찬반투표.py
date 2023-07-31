t = int(input())

vote = 0
invalid_cnt = 0
is_invalid = False

for i in tuple(map(int, input().split())):
    if ((t % 2 == 0 and t // 2 <= invalid_cnt) or
        (t % 2 != 0 and t // 2 < invalid_cnt)):
            is_invalid = True
            break
    
    if i == 0:
        invalid_cnt += 1
    elif 0 < i:
        vote += 1
    elif i < 0:
        vote -= 1

if is_invalid:
    print('INVALID')
elif (not is_invalid) and 0 < vote:
    print('APPROVED')
elif (not is_invalid) and vote <= 0:
    print('REJECTED')