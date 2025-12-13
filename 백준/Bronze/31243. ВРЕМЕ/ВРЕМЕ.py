def time_to_minute(h, m):
    return (h * 60) + m

def minute_to_time(m):
    return f'{m // 60}:{str(m % 60).zfill(2)}'

time_list = []

for _ in range(3):
    sh, sm, eh, em = map(int, input().split())

    t1 = time_to_minute(sh, sm)
    t2 = time_to_minute(eh, em)

    if t2 < t1:
        t2 += 1440

    time_list.append(t2 - t1)

time_list.sort()

print(minute_to_time(time_list[0]))
print(minute_to_time(time_list[-1]))