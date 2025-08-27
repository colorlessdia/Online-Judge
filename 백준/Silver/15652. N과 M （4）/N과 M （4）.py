def back_track(current_number, current_sequence, all_sequence):

    if M == len(current_sequence):
        all_sequence.append(list(current_sequence))
        return
    
    for i in range(current_number, N + 1):
        current_sequence.append(i)

        back_track(i, current_sequence, all_sequence)

        current_sequence.pop()

N, M = map(int, input().split())

all_sequence = []

back_track(1, [], all_sequence)

for sequence in all_sequence:
    print(*sequence)