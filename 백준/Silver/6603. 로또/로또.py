import sys

def back_track(index, k, s, current_sequence, all_sequence):

    if len(current_sequence) == 6:
        all_sequence.append(list(current_sequence))
        return
    
    if k - index < 6 - len(current_sequence):
        return

    for i in range(index, k):

        if len(current_sequence) + k - i < 6:
            continue

        current_sequence.append(s[i])
        back_track(i + 1, k, s, current_sequence, all_sequence)

        current_sequence.pop()

input = sys.stdin.readline

is_first = True

while 1:
    line = list(map(int, input().split()))

    if line[0] == 0:
        break

    K, S = line[0], line[1:]
    results = []

    back_track(0, K, S, [], results)

    if not is_first:
        print()

    for sequence in results:
        print(*sequence)
    
    is_first = False