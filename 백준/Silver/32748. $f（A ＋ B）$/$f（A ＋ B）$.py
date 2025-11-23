def f(N):
    return int(''.join([str(digit.index(int(n))) for n in str(N)]))

digit = list(map(int, input().split()))
A, B = map(int, input().split())

FAB = f(A) + f(B)

print(int(''.join([str(digit[int(number)]) for number in str(FAB)])))