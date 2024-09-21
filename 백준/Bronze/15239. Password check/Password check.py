import sys

N = int(sys.stdin.readline())

for _ in range(N):
    S = int(sys.stdin.readline())
    password = sys.stdin.readline().rstrip()

    is_valid = False

    has_lower = False
    has_upper = False
    has_number = False
    has_sign = False
    length = 0

    for char in password:
        length += 1

        if char.isdigit() and not has_number:
            has_number = True
            continue
        
        if char.islower() and not has_lower:
            has_lower = True
            continue
        
        if char.isupper() and not has_upper:
            has_upper = True
            continue

        if char in '+_)(*&^%$#@!./,;}{' and not has_sign:
            has_sign = True
            continue

    if (
        12 <= length and
        all([has_number, has_lower, has_upper, has_sign])
    ):
        is_valid = True
    
    if is_valid:
        print('valid')
    else:
        print('invalid')