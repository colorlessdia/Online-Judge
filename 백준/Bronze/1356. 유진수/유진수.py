n = input()

is_true = False

for i in range(1, len(n)):
    num1 = 1
    for j in list(n[:i]):
        num1 *= int(j)
    
    num2 = 1
    for k in list(n[i:]):
        num2 *= int(k)

    if num1 == num2:
        is_true = True
        break

print('YES') if is_true else print('NO')