N, M = map(int, input().split())
A_sequence = map(int, input().split())

rest_dict = {0: 1}
prefix_sum = 0
count = 0

for A in A_sequence:
    prefix_sum += A

    R = prefix_sum % M

    count += rest_dict.get(R, 0)
    rest_dict[R] = rest_dict.get(R, 0) + 1

print(count)