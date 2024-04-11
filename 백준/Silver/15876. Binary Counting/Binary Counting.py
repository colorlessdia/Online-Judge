n, k = map(int, input().split())

binary_number = 0
binary_string = ''

while len(binary_string) <=  n * 5:
    binary_string += bin(binary_number)[2:]

    binary_number += 1

binary_string = binary_string[:n * 5]

number_list = [binary_string[i] for i in range(k - 1, len(binary_string), n)]

print(*number_list)