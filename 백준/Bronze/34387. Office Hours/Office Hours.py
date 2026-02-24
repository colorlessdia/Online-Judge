import sys

input = sys.stdin.readline

days = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
]
schedule_count = {}

N = int(input())

for _ in range(N):
    line = input().rstrip().split()
    S, D = line[0], line[1]
    X_list = list(map(int, line[3:]))

    for X in X_list:
        K = (D, X)
        schedule_count[K] = schedule_count.get(K, 0) + 1

sorted_schedule = sorted(schedule_count.items(), key=lambda x: -x[1])
day, time = sorted_schedule[0][0]
time = str(time).zfill(2)

print(f'Your professor should host office hours {day} @ {time}:00')