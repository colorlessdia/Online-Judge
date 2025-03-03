N = int(input())
size_sequence = map(int, input().split())
T, P = map(int, input().split())

t_bundle = 0
p_bundle = N // P
p_each = 0 if N % P == 0 else N % P

for size in size_sequence:
    t_bundle += size // T

    if size % T != 0:
        t_bundle += 1

print(t_bundle)
print(p_bundle, p_each)