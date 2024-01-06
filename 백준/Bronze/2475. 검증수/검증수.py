code = list(map(int, input().split()))
chk_n = sum(list(map(lambda x: x*x, code))) % 10

print(chk_n)