import sys

scenario = 0

while True:
    o, w = map(int, sys.stdin.readline().split())

    if o == w == 0:
        break
    
    scenario += 1
    
    is_dead = False
    
    while True:
        line = sys.stdin.readline().rstrip()

        if line == '# 0':
            break
        
        action, n = line.split()

        if action == 'E':
            w -= int(n)
        elif action == 'F':
            w += int(n)
        
        if w <= 0:
            is_dead = True

    pet_state = ''

    if is_dead:
        pet_state = 'RIP'
    else:
        if o / 2 < w < o * 2:
            pet_state = ':-)'
        else:
            pet_state = ':-('

    print(f'{scenario} {pet_state}')