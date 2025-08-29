def back_track(current_sequence, all_sequence):

    if M == len(current_sequence):
        all_sequence.append(list(current_sequence))
        return
    
    for i in range(N):

        if not visited[i]:
            current_sequence.append(numbers[i])
            visited[i] = True

            back_track(current_sequence, all_sequence)

            current_sequence.pop()
            visited[i] = False

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))

visited = [False] * N
all_sequence = []
back_track([], all_sequence)

for sequence in all_sequence:
    print(*sequence)