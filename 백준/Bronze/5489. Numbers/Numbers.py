import sys

N = int(input())

number_frequency = dict()

for _ in range(N):
    number = int(sys.stdin.readline())

    if number in number_frequency:
        number_frequency[number] += 1
    else:
        number_frequency[number] = 1

result = sorted(number_frequency.items(), key=lambda x: (-x[1], x[0]))[0][0]

print(result)