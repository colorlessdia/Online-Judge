M = int(input())

cup_list = [1, 2, 3]

for _ in range(M):
    X, Y = map(lambda x: int(x) - 1, input().split())

    cup_list[Y], cup_list[X] = cup_list[X], cup_list[Y]

print(cup_list.index(1) + 1)