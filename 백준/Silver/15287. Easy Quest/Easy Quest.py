N = int(input())
A_sequence = list(map(int, input().split()))

is_valid = True
count_history = []
count_list = [0] * (1000 + 1)
unicorn_list = [] 

for A in A_sequence:
    
    if 0 < A:
        count_list[A] += 1
        continue

    if A == 0:
        unicorn_list.append(len(count_history))
        count_history.append(0)
        continue

    NA = -A
    
    if 0 < count_list[NA]:
        count_list[NA] -= 1
    elif unicorn_list:
        index = unicorn_list.pop(0)
        count_history[index] = NA
    else:
        is_valid = False
        break

if is_valid:

    for index in unicorn_list:
        count_history[index] = 1
        
    print('Yes')
    print(*(count_history))
else:
    print('No')