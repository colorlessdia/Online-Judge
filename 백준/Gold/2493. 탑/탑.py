from collections import deque

N = int(input())
send_list = list(map(int, input().split()))
reception_list = [0] * N

stack = deque()

for i in range(N):
    send_number = i + 1
    send_height = send_list[i]

    while 0 < len(stack):
        reception_number, reception_height = stack[-1]
        
        if send_height <= reception_height:
            reception_list[i] = reception_number
            stack.append([send_number, send_height])
            break
        
        stack.pop()

    if len(stack) == 0:
        reception_list[i] = 0
        stack.append([send_number, send_height])
        continue

print(*reception_list)