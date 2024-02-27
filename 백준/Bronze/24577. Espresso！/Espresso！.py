import sys

n, s = map(int, input().split())

water_tank = s
count = 0

for _ in range(n):
    order = sys.stdin.readline().rstrip()

    oz = 0

    if order[-1] == 'L':
        oz = int(order[0]) + 1
    else:
        oz = int(order[0])

    if water_tank < oz:
        water_tank = s - oz
        count += 1
    else:
        water_tank -= oz

print(count)