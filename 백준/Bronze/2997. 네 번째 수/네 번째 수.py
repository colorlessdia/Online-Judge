a, b, c = sorted(map(int, input().split()))

difference_1 = b - a
difference_2 = c - b

if difference_1 == difference_2:
    if c + difference_2 < 100:
        print(c + difference_2)
    else:
        print(a - difference_2)
else:
    if difference_2 < difference_1:
        print(b - difference_2)
    else:
        print(c - difference_1)

print(difference_1, difference_2)