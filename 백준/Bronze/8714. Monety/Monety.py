N = int(input())
number_sequence = map(int, input().split())

front = 0
back = 0

for number in number_sequence:

    if number == 1:
        front += 1
    else:
        back += 1

if front < back:
    print(front)
else:
    print(back)