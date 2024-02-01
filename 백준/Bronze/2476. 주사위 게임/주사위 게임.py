import sys

N = int(input())

reward_list = [0] * N

for i in range(N):
    dice_1, dice_2, dice_3 = map(int, sys.stdin.readline().split())

    reward = 0

    if dice_1 == dice_2 == dice_3:
        reward = 10000 + dice_1 * 1000
    elif dice_1 == dice_2 or dice_1 == dice_3:
        reward = 1000 + dice_1 * 100
    elif dice_2 == dice_3:
        reward = 1000 + dice_2 * 100
    else:
        reward = 100 * max(dice_1, dice_2, dice_3)
    
    reward_list[i] = reward

print(max(reward_list))