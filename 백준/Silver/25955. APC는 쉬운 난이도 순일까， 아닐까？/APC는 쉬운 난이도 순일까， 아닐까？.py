def formatted_level(level):
    matched_tier = dict(zip(list('BSGPD'), list(range(5))))

    tier = matched_tier[level[0]]
    step = int(level[1:])

    return (tier, step, level)

N = int(input())
level_list = list(map(formatted_level, input().split()))

sorted_level_list = sorted(level_list, key=lambda x: (x[0], -x[1]))

is_sorted = True
index_list = []

for i, (level, sorted_level) in enumerate(zip(level_list, sorted_level_list)):
    
    if level[-1] != sorted_level[-1]:
        is_sorted = False
        index_list.append(i)

if is_sorted:
    print('OK')
else:
    target_level_1 = sorted_level_list[index_list[0]][-1]
    target_level_2 = sorted_level_list[index_list[1]][-1]
    
    print('KO')
    print(target_level_1, target_level_2)