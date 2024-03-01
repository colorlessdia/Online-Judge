X, Y, Z = sorted(map(int, input().split()))

min_number = 0

if X == 0 and Y == 0:
    min_number = int(str(Z) + str(X) + str(Y))
elif X == 0:
    min_number = int(str(Y) + str(X) + str(Z))
else:
    min_number = int(str(X) + str(Y) + str(Z))

print(min_number)