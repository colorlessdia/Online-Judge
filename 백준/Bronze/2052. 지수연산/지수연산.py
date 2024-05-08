N = int(input())

float_string = '%.300f' % (1 / (2 ** N))

zero_count = 0

for float_char in float_string[::-1]:
    if float_char != '0':
        break
    
    zero_count += 1

print(float_string[:len(float_string) - zero_count])