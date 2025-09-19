A, B = map(int, input().split())
M = int(input())
number_list = list(map(int, input().split()))

decimal_number = 0

for i in range(M):
    decimal_number += number_list[i] * (A ** (M - 1 - i))

result_list = []

if decimal_number == 0:
    print(0)
else:

    while 0 < decimal_number:
        result_list.append(decimal_number % B)
        decimal_number //= B

    print(*result_list[::-1])