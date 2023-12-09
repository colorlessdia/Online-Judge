price = int(input())

for i in range(1000, 9900 + 100, 100):
    if int(i * 1.1) == price:
        print(i)