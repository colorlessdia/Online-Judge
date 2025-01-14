matched_month = {
    '': 0,
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}
matched_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

M, D, Y, T = input().split()

M = matched_month[M]
D = int(D[:-1])
Y = int(Y)
HH, MM = map(int, T.split(':'))

if Y % 400 == 0 or (Y % 4 == 0 and Y % 100 != 0):
    matched_day[2] += 1

year_to_second = sum(matched_day) * 24 * 60
current_to_second = ((sum(matched_day[:M]) + D - 1) * (24 * 60)) + (HH * 60) + MM

print((current_to_second / year_to_second) * 100)