K = int(input())

i = 1
a = 1
b = 2

while not(a <= K <= b):
    i += 1

    c = 2 ** i
    a = b + 1
    b = a + c - 1

number_list = [0] * i

j = 0

while 1:
    d = b - a
    
    if d == 1:

        if K % 2 == 1:
            number_list[j] = '4'
        else:
            number_list[j] = '7'

        break
    
    e = d // 2

    if a <= K <= a + e:
        b = a + e
        number_list[j] = '4'
    else:
        a = b - e
        number_list[j] = '7'

    j += 1

print(''.join(number_list))