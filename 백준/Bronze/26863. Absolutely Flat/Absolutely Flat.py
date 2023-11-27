leg = sorted([int(input()) for _ in range(4)])
pad = int(input())

if all(l == leg[0] for l in leg) == True:
    print(1)
elif all(l == leg[0] + pad for l in leg[1:]) == True:
    print(1)
else:
    print(0)