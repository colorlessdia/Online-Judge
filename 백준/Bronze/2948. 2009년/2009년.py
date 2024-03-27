D, M = map(int, input().split())

date_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year_2009 = dict(zip(map(str, range(1, 12 + 1)), date_list))

date, month = 1, 1

week_list = ['Thurs', 'Fri', 'Satur', 'Sun', 'Mon', 'Tues', 'Wednes']
week_index = 0

while True:
    if D == date and M == month:
        break

    if date + 1 <= year_2009[str(month)]:
        date += 1
    else:
        date = 1
        month += 1

    if week_index + 1 < 7:
        week_index += 1
    else:
        week_index = 0

print(f'{week_list[week_index]}day')