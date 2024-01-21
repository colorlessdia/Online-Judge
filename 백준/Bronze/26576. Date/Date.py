import sys

N = int(input())

month_list = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]

for _ in range(N):
    month, date, year = sys.stdin.readline().rstrip().split()

    if month in month_list and 1 <= int(date[:-1]) <= 31:
        formatted_month, formatted_date, formatted_year = '', '', ''

        if len(str(month_list.index(month) + 1)) == 1:
            formatted_month = '0' + str(month_list.index(month) + 1)
        else:
            formatted_month = str(month_list.index(month) + 1)

        if len(date[:-1]) == 1:
            formatted_date = '0' + date[:-1]
        else:
            formatted_date = date[:-1]
        
        if len(year) == 1:
            formatted_year = '0' + year
        else:
            formatted_year = year[-2:]

        print(f'{formatted_month}/{formatted_date}/{formatted_year}')
    else:
        print('Invalid')