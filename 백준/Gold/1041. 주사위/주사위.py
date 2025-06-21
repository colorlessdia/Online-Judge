N = int(input())
number_list = [0] + list(map(int, input().split()))

best_1 = min(number_list[1:])
best_2 = 2000001
best_3 = 3000001

for i in range(1, 6 + 1):

    for j in range(i + 1, 6 + 1):
        
        if (i, j) in [(1, 6), (2, 5), (3, 4)]:
            continue
        
        sum_2 = number_list[i] + number_list[j]

        if sum_2 < best_2:
            best_2 = sum_2

combination_list = [
    (1, 2, 3),
    (1, 2, 4),
    (1, 3, 5),
    (1, 4, 5),
    (2, 3, 6),
    (2, 4, 6),
    (3, 5, 6),
    (4, 5, 6)
]

for combination in combination_list:
    sum_3 = 0
    
    for number in combination:
        sum_3 += number_list[number]
    
    if sum_3 < best_3:
        best_3 = sum_3

if N == 1:
    print(sum(number_list) - max(number_list))
elif N == 2:
    print((best_2 * 4) + (best_3 * 4))
else:
    v_1 = ((N - 1) * (N - 2) * 4) + ((N - 2) ** 2)
    v_2 = (((N ** 2) * 5) - v_1 - 12) // 2

    b_1 = best_1 * v_1
    b_2 = best_2 * v_2
    b_3 = best_3 * 4

    print(b_1 + b_2 + b_3)