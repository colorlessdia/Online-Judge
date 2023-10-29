n = int(input())

pow_list = [2 ** i for i in range(30 + 1)]

print(1) if n in pow_list else print(0)