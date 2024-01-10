P, N = map(int, input().split())
A = list(map(int, input().split()))

fatigue = P
count = 0

for a in sorted(A):
    if 200 <= fatigue:
        break
    
    fatigue += a
    count += 1
    
print(count)