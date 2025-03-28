S = input()

number_list = [0] + list(map(int, list(S)))

S_length = len(S)
prefix_sum = [0] * (S_length + 1)

for i in range(1, S_length + 1):
    prefix_sum[i] = prefix_sum[i - 1] + number_list[i]

length = S_length if S_length % 2 == 0 else S_length - 1
is_find = False

for j in range(length, 1, -2):
    
    if is_find:
        break

    for k in range(S_length - j + 1):
        start = k
        end = k + j
        middle = end - ((end - start) // 2)

        front_sum = prefix_sum[middle] - prefix_sum[start]
        back_sum = prefix_sum[end] - prefix_sum[middle]

        if front_sum == back_sum:
            length = j
            is_find = True
            break

if is_find:
    print(length)
else:
    print(0)