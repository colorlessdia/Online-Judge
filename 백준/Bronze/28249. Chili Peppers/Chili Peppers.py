import sys

matched_pepper = dict(zip(['Poblano', 'Mirasol', 'Serrano', 'Cayenne', 'Thai', 'Habanero'], [1500, 6000, 15500, 40000, 75000, 125000]))
shu = 0

for _ in range(int(input())):
    pepper = sys.stdin.readline().rstrip()

    shu += matched_pepper[pepper]

print(shu)