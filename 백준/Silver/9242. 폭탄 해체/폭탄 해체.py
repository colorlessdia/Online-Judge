code_list = [[] for _ in range(8)]

matched_number = {
    '**** ** ** ****': '0',
    '  *  *  *  *  *': '1',
    '***  *****  ***': '2',
    '***  ****  ****': '3',
    '* ** ****  *  *': '4',
    '****  ***  ****': '5',
    '****  **** ****': '6',
    '***  *  *  *  *': '7',
    '**** ***** ****': '8',
    '**** ****  ****': '9'
}

for i in range(5):
    line = input()

    temp = ''
    index = 0

    for j, char in enumerate(line, 1):
        
        if j % 4 == 0:
            code_list[index].append(temp)
            temp = ''
            index += 1
            continue
    
        temp += char
    
    code_list[index].append(temp)

in_valid = True
number = ''

for code in code_list:

    if len(code) == 0:
        continue
    
    string = ''.join(code)

    if string not in matched_number:
        in_valid = False
        break
    
    number += matched_number[string]

if in_valid:
    
    if int(number) % 6 == 0:
        print('BEER!!')
    else:
        print('BOOM!!')
else:
    print('BOOM!!')