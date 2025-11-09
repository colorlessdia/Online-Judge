S = input()

A, B = 0, 0

for char in S:

    if char in 'aeiou':
        A += 1
        B += 1
    
    if char == 'y':
        B += 1

print(A, B)