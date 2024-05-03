x, y = map(int, input().split())

date_range = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_range = list(range(1, 12 + 1))
year_2007 = dict(zip(month_range, date_range))

month = 1
date = 1

week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
week_index = 0

while True:
    if x == month and y == date:
        break

    if year_2007[month] < date + 1:
        month += 1
        date = 1
    else:
        date += 1

    if len(week) == week_index + 1:
        week_index = 0
    else:
        week_index += 1

print(week[week_index])