import string

upper_alphabat = string.ascii_uppercase

column = input()
length = len(column)

column_order = 0

for i, alphabat in enumerate(column[::-1], 1):
    column_order += (upper_alphabat.index(alphabat) + 1) * (26 ** (i - 1))

print(column_order)