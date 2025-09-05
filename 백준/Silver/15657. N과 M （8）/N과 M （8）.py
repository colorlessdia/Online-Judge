def back_track(index, current_sequence, all_sequence):

    if M == len(current_sequence):
        all_sequence.append(list(current_sequence))
        return
    
    for i in range(index, N):
        number = numbers[i]

        current_sequence.append(number)
        back_track(i, current_sequence, all_sequence)

        current_sequence.pop()

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))

results = []
back_track(0, [], results)

for result in results:
    print(*result)