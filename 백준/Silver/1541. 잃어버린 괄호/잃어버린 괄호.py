S = input()

number_list = []
temp = ''

for i in range(len(S) + 1):

    if i == len(S):
        number_list.append(int(temp))
        break
    
    char = S[i]
    
    if i == 0 and char == '-':
        temp = '-'
        continue

    if char.isnumeric():
        temp += char
        continue
    
    number_list.append(int(temp))
    temp = char

total = 0
is_negative = False

for number in number_list:

    if number < 0:
        is_negative = True

    if is_negative and 0 <= number:
        number *= -1

    total += number

print(total)