import sys

n = int(sys.stdin.readline())

number_list = []

for _ in range(n):
    text = sys.stdin.readline().rstrip()

    temp = ''
    
    for char in text:
        
        if char.isdigit():
            temp += char
            continue
        
        if len(temp) != 0:
            number_list.append(int(temp))
            temp = ''
    
    if len(temp) != 0:
        number_list.append(int(temp))

sorted_number_list = sorted(number_list)

for number in sorted_number_list:
    print(number)