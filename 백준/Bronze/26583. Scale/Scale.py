import sys

while True:
    line = sys.stdin.readline().rstrip()

    if line == '':
        break
    
    number_list = list(map(int, line.split()))

    calculated_number_list = [0] * len(number_list)

    for i in range(len(number_list)):
        number = 1

        if i == 0:
            number = number_list[i] * number_list[i + 1]
        elif i == len(number_list) - 1:
            number = number_list[i] * number_list[i - 1]
        else:
            number = number_list[i] * number_list[i + 1] * number_list[i - 1]
        
        calculated_number_list[i] = number

    formatted_number_list = ' '.join(map(str, calculated_number_list))

    print(f'{formatted_number_list}')