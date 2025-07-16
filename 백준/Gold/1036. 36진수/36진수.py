import sys

def decimal_to_base36(D, matched_char):

    if D == 0:
        return '0'
    
    R_list = []

    while 0 < D:
        R = D % 36
        R_list.append(matched_char[R])
        D //= 36
    
    return ''.join(reversed(R_list))

input = sys.stdin.readline

N = int(input())

k = list(map(str, range(10)))
k.extend([chr(i) for i in range(ord('A'), ord('Z') + 1)])
v = list(range(36))

matched_number = dict(zip(k,  v))
matched_char = dict(zip(v, k))
number_count = dict()

base36_list = [0] * N

for i in range(N):
    base36 = input().rstrip()
    base36_list[i] = base36

    for j, number in enumerate(reversed(base36)):
        number_value = matched_number[number]

        if number not in number_count:
            number_count[number] = 0
        
        number_count[number] += (35 - number_value) * (36 ** j)

K = int(input())

sorted_count = sorted(number_count.items(), key=lambda x: (-x[1], x[0]))
change_number = set()

while 0 < K and sorted_count:
    number, _ = sorted_count.pop(0)
    change_number.add(number)

    K -= 1

decimal = 0

for base36 in base36_list:
    
    for i, number in enumerate(reversed(base36)):

        if number in change_number:
            decimal += (35 * (36 ** i))
            continue

        decimal += (matched_number[number] * (36 ** i))

print(decimal_to_base36(decimal, matched_char))