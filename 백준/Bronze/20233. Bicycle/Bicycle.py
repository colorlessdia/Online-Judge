a, x, b, y, T = [int(input()) for _ in range(5)]

a_fee = a
b_fee = b

for _ in range(21):
    if 30 < T:
        a_fee += (T - 30) * x
    
    if 45 < T:
        b_fee += (T - 45) * y

print(a_fee, b_fee)