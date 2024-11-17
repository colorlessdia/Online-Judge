import sys

T = int(sys.stdin.readline())

date_minute = 60 * 24
year_minute = date_minute * 365

for _ in range(T):
    game, playtime = sys.stdin.readline().rstrip().split(',')
    playtime = int(playtime)

    year = playtime // year_minute
    day = playtime % year_minute // date_minute
    hour = playtime % year_minute % date_minute // 60
    minute = playtime % year_minute % date_minute % 60

    formatted_text = f'{game} -'

    if year != 0:
        formatted_text += f' {year} year(s)'

    if day != 0:
        formatted_text += f' {day} day(s)'

    if hour != 0:
        formatted_text += f' {hour} hour(s)'

    if minute != 0:
        formatted_text += f' {minute} minute(s)'

    print(formatted_text)