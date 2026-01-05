import sys

input = sys.stdin.readline

N = int(input())

target_restaurant = []

for _ in range(N):
    K = int(input())
    restaurant = input().rstrip()

    checked_menu = [0, 0]

    for _ in range(K):
        menu = input().rstrip()

        if menu == 'pea soup':
            checked_menu[0] = 1
        elif menu == 'pancakes':
            checked_menu[1] = 1
    
    if all(checked_menu) and (not target_restaurant):
        target_restaurant.append(restaurant)

if target_restaurant:
    print(*target_restaurant)
else:
    print('Anywhere is fine I guess')