import sys

def GCD(x, y):
    
    if y == 0:
        return x

    return GCD(y, x % y)

number_list = []

while True:
    line = sys.stdin.readline().rstrip()

    if line == '':
        break
    
    number_list += list(map(int, line.split()))

sorted_number_list = sorted(number_list)

max_GCD = 0

for i in range(len(sorted_number_list)):
    
    for j in range(i + 1, len(sorted_number_list)):
        x, y = sorted_number_list[j], sorted_number_list[i]

        gcd = GCD(x, y)

        if max_GCD < gcd:
            max_GCD = gcd
    
print(max_GCD)