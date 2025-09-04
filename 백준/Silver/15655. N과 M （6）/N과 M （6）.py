def back_track(index, current_sequence, all_sequence):

    if M == len(current_sequence):
        all_sequence.append(list(current_sequence))
        return

    for i in range(index, N):

        if visited[numbers[i]]:
            continue

        current_sequence.append(numbers[i])
        visited[numbers[i]] = True
        back_track(i + 1, current_sequence, all_sequence)

        current_sequence.pop()
        visited[numbers[i]] = False

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))

visited = [False] * (numbers[-1] + 1)
results = []
back_track(0, [], results)

for result in results:
    print(*result)