import sys

cancelled_year = [1916, 1940, 1944]
olympic_year = [i for i in range(1896, 2028 + 1, 4) if i not in cancelled_year]

while True:
    year = int(sys.stdin.readline())

    if year == 0:
        break

    message = ''

    if year in olympic_year and (year < 2024):
        message = 'Summer Olympics'
    elif year in olympic_year:
        message = 'No city yet chosen'
    elif year in cancelled_year:
        message = 'Games cancelled'
    else:
        message = 'No summer games'

    print(f'{year} {message}')