line = input()
file, rank = line[0], line[1]

f = ord(file)
r = int(rank)

df = [-2, -1, 1, 2, 2, 1, -1, -2]
dr = [1, 2, 2, 1, -1, -2, -2, -1]

coordinate_list = []

for i in range(8):
    F = f + df[i]
    R = r + dr[i]

    if (ord('a') <= F <= ord('h')) and (1 <= R <= 8):
        coordinate = ''.join([chr(F), str(R)])
        coordinate_list.append(coordinate)

coordinate_list.sort(key=lambda x: (x[0], x[1]))

for coordinate in coordinate_list:
    print(coordinate)