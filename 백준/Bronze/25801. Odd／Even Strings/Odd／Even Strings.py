S = input()

k = [chr(i) for i in range(ord('a'), ord('z') + 1)]
v = [0] * 26
char_count = dict(zip(k, v))

check_even_odd = [0, 0]

for s in S:
    char_count[s] += 1

for v in char_count.values():
    
    if v == 0:
        continue

    if v % 2 == 0:
        check_even_odd[0] += 1
    else:
        check_even_odd[1] += 1

even, odd = check_even_odd

if even and odd:
    print('0/1')
elif even:
    print('0')
elif odd:
    print('1')