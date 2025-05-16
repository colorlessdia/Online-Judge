import sys

input = sys.stdin.readline

cow_list = [
    'Bessie', 
    'Elsie', 
    'Daisy', 
    'Gertie', 
    'Annabelle', 
    'Maggie', 
    'Henrietta'
]
milk_count = dict(zip(cow_list, [0] * 7))

N = int(input())

for _ in range(N):
    cow, milk = input().rstrip().split()

    milk_count[cow] += int(milk)

M = min(milk_count.values())

min_cow_list = []

for cow, milk in milk_count.items():
    
    if milk == M:
        min_cow_list.append(cow)

for min_cow in min_cow_list:
    
    del milk_count[min_cow]

sorted_milk = sorted(milk_count.items(), key=lambda x: x[1])

if len(sorted_milk) == 0:
    print('Tie')
elif 1 < len(sorted_milk) and sorted_milk[0][1] == sorted_milk[1][1]:
    print('Tie')
else:
    print(sorted_milk[0][0])