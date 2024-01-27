X = input()

count = 0

while True:
    if len(X) == 1:
        print(count)
        break
    
    count += 1

    Y = 0

    for x in X:
        Y += int(x)
    
    X = str(Y)

if int(X) % 3 == 0:
    print('YES')
else:
    print('NO')