line = input()

cup_list = [0, 1, 0, 0]

for char in line:
    if char == 'A':
        cup_list[1], cup_list[2] = cup_list[2], cup_list[1]
    elif char == 'B':
        cup_list[2], cup_list[3] = cup_list[3], cup_list[2]
    elif char == 'C':
        cup_list[1], cup_list[3] = cup_list[3], cup_list[1]

print(cup_list.index(1))