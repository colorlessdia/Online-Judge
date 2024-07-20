pizza_list = [int(input()) for _ in range(8)]

mushroom_count = []

for i in range(8):
    total_mushroom = 0

    if i + 4 < len(pizza_list):
        total_mushroom = sum(pizza_list[i:i + 4])
    else:
        total_mushroom = sum(pizza_list[i:] + pizza_list[:i + 4 - len(pizza_list)])

    mushroom_count.append(total_mushroom)

print(max(mushroom_count))