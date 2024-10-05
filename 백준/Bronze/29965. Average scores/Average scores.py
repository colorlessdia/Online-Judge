import sys

M, m = 0, 0
J, j = 0, 0

N = int(sys.stdin.readline())

for _ in range(N):
    C, P = sys.stdin.readline().rstrip().split()

    if C == 'M':
        M += int(P)
        m += 1
    elif C == 'J':
        J += int(P)
        j += 1

M_score = 0
J_score = 0

if m != 0:
    M_score = M / m
if j != 0:
    J_score = J / j

if M_score == J_score:
    print('V')
elif J_score < M_score:
    print('M')
elif M_score < J_score:
    print('J')