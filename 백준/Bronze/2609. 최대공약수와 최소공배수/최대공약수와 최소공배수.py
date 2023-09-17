a, b = map(int, input().split())
aa, bb = max(a, b), min(a, b)

gcd, lcm = 0, 0

while 1:
    if aa % bb == 0:
        gcd = bb
        break

    aa, bb = bb, aa % bb

lcm = int((a * b) / gcd)

print(gcd)
print(lcm)