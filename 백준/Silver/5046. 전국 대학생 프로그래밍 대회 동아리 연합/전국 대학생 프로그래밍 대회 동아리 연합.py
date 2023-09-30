n, b, h, w = map(int, input().split())

money = []

for _ in range(h):
    p = int(input())
    a = map(int, input().split())

    for aa in a:
        if n <= aa and n * p <= b:
            money.append(n * p)

sort_money = sorted(money)

print('stay home') if len(money) == 0 else print(sort_money[0])