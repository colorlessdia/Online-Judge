N = int(input())
A_list = list(map(int, input().split()))

number_list = []
index = 0

while index < N:
    number = A_list[index]
    number_list.append(number)

    index += number

print(*number_list)