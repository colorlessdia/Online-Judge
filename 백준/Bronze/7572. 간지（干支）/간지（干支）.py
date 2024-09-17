year = int(input())

sexagenary_cycle = [0] * 60

zodiac_sign = 'ABCDEFGHIJKL'
ten_years = '0123456789'

sign_index = 0
year_index = 0

for i in range(60):
    sexagenary = zodiac_sign[sign_index] + ten_years[year_index]
    sexagenary_cycle[i] = sexagenary

    sign_index += 1
    year_index += 1

    if 12 <= sign_index:
        sign_index = 0
    
    if 10 <= year_index:
        year_index = 0

index = (year % 60) - 4

print(sexagenary_cycle[index])