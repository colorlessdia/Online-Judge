import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    message = list(input().rstrip())
    message.append(' ')

    compress_list = []
    s, e = 0, 1

    while e < len(message):
        start_char = message[s]
        end_char = message[e]

        if start_char == end_char:
            e += 1
            continue

        compress_list.append(str(len(message[s:e])))
        compress_list.append(message[s])

        s = e
        e = s + 1
    
    print(' '.join(compress_list))