n = input()

if '7' not in n:
    print(0) if int(n) % 7 != 0 else print(1)
else:
    print(2) if int(n) % 7 != 0 else print(3)