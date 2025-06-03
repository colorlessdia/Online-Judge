import sys

input = sys.stdin.readline

N = int(input())

schedule_list = [list(map(int, input().split())) for _ in range(N)]
schedule_list.sort(key=lambda x: (x[1], x[0]))

before_schedule = schedule_list[0]
count = 1

if N == 1:
    print(count)
else:
    
    for current_schedule in schedule_list[1:]:
        before_end = before_schedule[1]
        current_start = current_schedule[0]

        if before_end <= current_start:
            before_schedule = current_schedule
            count += 1
    
    print(count)