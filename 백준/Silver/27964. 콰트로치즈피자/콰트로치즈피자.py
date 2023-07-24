n = int(input())
cheese_list = input().split()
cheese_dict = dict()

for cheese in cheese_list:
    if cheese[-6:] != 'Cheese':
        continue
    
    if cheese in cheese_dict:
        cheese_dict[cheese] += 1
    else:
        cheese_dict[cheese] = 1

if 4 <= len(cheese_dict):
    print('yummy')
else:
    print('sad')