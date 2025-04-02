def time_to_second(h, m, s):
    return (h * 60 * 60) + (m * 60) + s

def second_to_time(time):
    h = time // (60 * 60)
    m = time % (60 * 60) // 60
    s = time % (60 * 60) % 60

    return (h, m, s)

for _ in range(3):
    sh, sm, ss, eh, em, es = map(int, input().split())

    start = time_to_second(sh, sm, ss)
    end = time_to_second(eh, em, es)

    difference = end - start

    print(*second_to_time(difference))