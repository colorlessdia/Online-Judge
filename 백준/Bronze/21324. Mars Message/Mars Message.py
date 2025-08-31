import sys

input = sys.stdin.readline

N = int(input())

matched_hex = list('0123456789abcdef')
message = []
temp = []

for i in range(N):
    A = int(float(input()) / 22.5)

    temp.append(matched_hex[A])

    if i % 2 == 1:
        message.append(chr(int(''.join(temp), 16)))
        temp.clear()

print(''.join(message))