w = input()

alphabat_count = [0] * 26

for char in w:
    index = ord(char) - ord('a')

    alphabat_count[index] += 1

if alphabat_count.count(0) != 0:
    print(alphabat_count.count(0))
else:
    print('impossible')