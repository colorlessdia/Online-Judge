N = int(input())
S = input()

box_list = [0, 1, 0, 0]

ball = box_list.index(1)
count = 0

for char in S:
    if char == 'L' and ball != 1:
        box_list[ball] = 0
        box_list[ball - 1] = 1
        ball -= 1
    elif char == 'R' and ball != 3:
        box_list[ball] = 0
        box_list[ball + 1] = 1
        ball += 1
    
    if ball == 3:
        count += 1

print(count)