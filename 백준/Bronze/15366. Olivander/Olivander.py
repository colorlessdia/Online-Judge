N = int(input())
X_list = sorted(map(int, input().split()))
Y_list = sorted(map(int, input().split()))

is_valid = True

for X, Y in zip(X_list, Y_list):

    if Y < X:
        is_valid = False
        break

if is_valid:
    print('DA')
else:
    print('NE')