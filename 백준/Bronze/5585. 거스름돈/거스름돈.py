price = int(input())

coin_list = [500, 100, 50, 10, 5, 1]
target = 1000 - price

cnt = 0

for coin in coin_list:
    cnt += target // coin
    target %= coin

print(cnt)