N = int(input())
A = list(map(int, input().split()))

max_age = max(A)
min_age = min(A)

for age in A:
    difference1 = abs(max_age - age)
    difference2 = abs(min_age - age)

    print(max(difference1, difference2))