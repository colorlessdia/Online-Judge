N = int(input())
S = input()

lower_rainbow = set()
upper_rainbow = set()

for s in S:
    
    if s in 'roygbiv':
        lower_rainbow.add(s)
        continue

    if s in 'ROYGBIV':
        upper_rainbow.add(s)

lower_length = len(lower_rainbow)
upper_length = len(upper_rainbow)

if 7 == lower_length == upper_length:
    print('YeS')
elif 7 == lower_length:
    print('yes')
elif 7 == upper_length:
    print('YES')
else:
    print('NO!')