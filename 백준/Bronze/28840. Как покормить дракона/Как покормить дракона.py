def time_to_minute(time):
    HH, MM = time

    return (HH * 60) + MM

def minute_to_time(minute):
    HH = str(minute // 60).rjust(2, '0')
    MM = str(minute % 60).rjust(2, '0')

    return f'{HH}:{MM}'

time_1 = time_to_minute(list(map(int, input().split(':'))))
time_2 = time_to_minute(list(map(int, input().split(':'))))

midnight = 60 * 24

if time_1 == time_2:
    print(minute_to_time(midnight))
else:
    print(minute_to_time(midnight - time_1 + time_2))