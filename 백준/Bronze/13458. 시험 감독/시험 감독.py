N = int(input())
A_list = list(map(int, input().split()))
B, C = map(int, input().split())

count = 0

for A in A_list:
    
    if A <= B:
        count += 1
        continue
    
    count += ((A - B) // C) + 1

    if (A - B) % C != 0:
        count += 1

print(count)