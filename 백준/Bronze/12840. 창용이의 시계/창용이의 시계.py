import sys

def second_to_time(second):
    second %= 86400

    hh = second // 3600
    mm = second % 3600 // 60
    ss = second % 3600 % 60

    return (hh, mm, ss)

def time_to_second(h, m, s):
    return (h * 3600) + (m * 60) + s

h, m, s = map(int, sys.stdin.readline().split())
q = int(sys.stdin.readline())

for _ in range(q):
    query = sys.stdin.readline().rstrip().split()

    if query[0] == '1':
        calc_second = (time_to_second(h, m, s) + int(query[1])) % 86400
        h, m, s = second_to_time(calc_second)
    elif query[0] == '2':
        calc_second = time_to_second(h, m, s) - int(query[1])

        if calc_second < 0:
            calc_second = 86400 - (-calc_second % 86400)
            
        h, m, s = second_to_time(calc_second)
    elif query[0] == '3':
        print(h, m, s)