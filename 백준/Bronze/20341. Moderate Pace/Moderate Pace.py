n = int(input())
k, a, b = [map(int, input().split()) for _ in range(3)]

print(*[sorted(distance)[1] for distance in zip(k, a, b)])