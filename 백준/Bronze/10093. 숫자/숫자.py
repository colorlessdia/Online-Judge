A, B = map(int, input().split())

min_number = min(A, B)
max_number = max(A, B)

count = 0 if max_number - min_number <= 1 else max_number - min_number - 1

print(count)

for i in range(min_number + 1, max_number):
    
    if i < max_number - 1:
        print(i, end=' ')
        continue
    
    print(i, end='')