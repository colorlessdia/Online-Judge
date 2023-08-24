int(input())

for i in map(int, input().split()):
    num = sum([j for j in range(1, i + 1) if i % j == 0][:-1])
    
    if i == num:
        print('Perfect')
    elif num < i:
        print('Deficient')
    elif i < num:
        print('Abundant')