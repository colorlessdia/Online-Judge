import sys

input = sys.stdin.readline

while 1:
    N, M = map(int, input().split())

    if N == M == 0:
        break
    
    T_sequence = map(int, input().split())

    ticket_count = [0] * (N + 1)

    for T in T_sequence:
        ticket_count[T] += 1

    fake_ticket_count = 0

    for count in ticket_count[1:]:
        
        if 1 < count:
            fake_ticket_count += 1

    print(fake_ticket_count)