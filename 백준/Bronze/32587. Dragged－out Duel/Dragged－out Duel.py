N = int(input())
A = input()
B = input()

win_set = set([('R', 'S'), ('S', 'P'), ('P', 'R')])
A_count = 0
B_count = 0

for a, b in zip(A, B):
    
    if a == b:
        continue

    if (a, b) in win_set:
        A_count += 1
    else:
        B_count += 1

if B_count < A_count:
    print('victory')
else:
    print('defeat')