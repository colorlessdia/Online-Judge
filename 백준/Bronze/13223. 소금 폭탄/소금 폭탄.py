def time_to_second(h, m, s):
    return (h * 3600) + (m * 60) + s

def second_to_time(s):
    h = s // 3600
    m = s % 3600 // 60
    s = s % 60

    return (h, m, s)

def formatted_time(time):
    return ':'.join(map(lambda x: str(x).zfill(2), time))

h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

t1 = time_to_second(h1, m1, s1)
t2 = time_to_second(h2, m2, s2)
t3 = 0

if t2 <= t1:
    t3 = time_to_second(24, 0, 0) - t1 + t2
else:
    t3 = t2 - t1

print(formatted_time(second_to_time(t3)))