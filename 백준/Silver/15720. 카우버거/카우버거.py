B, C, D = map(int, input().split())

burger = sorted(map(int, input().split()), reverse=True)
side = sorted(map(int, input().split()), reverse=True)
drink = sorted(map(int, input().split()), reverse=True)

total_price = 0
sale_price = 0

count = min(B, C, D)

sale_menu = burger[:count] + side[:count] + drink[:count]
menu = burger[count:] + side[count:] + drink[count:]

for price in sale_menu:
    total_price += price
    sale_price += int(price * 0.9)

for price in menu:
    total_price += price
    sale_price += price

print(total_price)
print(sale_price)