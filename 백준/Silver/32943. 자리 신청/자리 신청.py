import sys

input = sys.stdin.readline

X, C, K = map(int, input().split())

history = [tuple(map(int, input().split())) for _ in range(K)]
history.sort(key=lambda x: x[0])

seat_state = dict()
student_state = dict()

for T, S, N in history:

    if S in seat_state:
        continue

    if N in student_state:
        B = student_state[N]
        del seat_state[B]

    seat_state[S] = N
    student_state[N] = S

sorted_state = sorted(seat_state.items(), key=lambda x: x[1])

for s, n in sorted_state:
    print(n, s)