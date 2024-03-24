import sys

N, M = map(int, input().split())

song_dict = dict()
note_count_dict = dict()

for _ in range(N):
    song = sys.stdin.readline().rstrip().split()

    T, S, A = song[0], song[1], ' '.join(song[2:2 + 3])

    song_dict[S] = A

    if A in note_count_dict:
        note_count_dict[A] += 1
    else:
        note_count_dict[A] = 1

for _ in range(M):
    note = sys.stdin.readline().rstrip()

    if note in note_count_dict and note_count_dict[note] == 1:
        for k, v in song_dict.items():
            if v == note:
                print(k)
                break
    elif note in note_count_dict:
        print('?')
    else:
        print('!')