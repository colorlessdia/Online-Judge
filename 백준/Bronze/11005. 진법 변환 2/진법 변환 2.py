N, B = map(int, input().split())

V = ord('A') - 10
R = ''

while 0 < N:
    r = N % B

    R += str(chr(r + V)) if 10 <= r else str(r)
    N //= B

result = R[::-1]

print(result)