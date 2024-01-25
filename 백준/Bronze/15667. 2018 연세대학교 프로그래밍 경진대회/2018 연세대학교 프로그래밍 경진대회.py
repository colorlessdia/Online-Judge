N = int(input())

K = 1

while True:
    flame = 1 + K + (K ** 2)

    if flame == N:
        print(K)
        break

    K += 1