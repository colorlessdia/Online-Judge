import sys

N = int(sys.stdin.readline())

for n in range(1, N + 1):
    invitation_count = dict()

    G = int(sys.stdin.readline())
    C_list = sys.stdin.readline().rstrip().split()

    for C in C_list:
        
        if C not in invitation_count:
            invitation_count[C] = 1
            continue
        
        del invitation_count[C]
    
    odd_guests = ' '.join(list(invitation_count.keys()))

    print(f'Case #{n}: {odd_guests}')