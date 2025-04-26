import sys

input = sys.stdin.readline

N = int(input())

schedule_dict = dict()
work_time_list = [4, 6, 4, 10]

for _ in range(N):

    for i in range(4):
        worker_list = input().rstrip().split()
        work_time = work_time_list[i]

        for worker in worker_list:
            
            if worker == '-':
                continue
            
            if worker not in schedule_dict:
                schedule_dict[worker] = work_time
                continue
            
            schedule_dict[worker] += work_time

is_fair = True

if len(schedule_dict) != 0:
    sorted_schedule = sorted(schedule_dict.items(), key=lambda x: x[1])

    maximum_schedule = sorted_schedule[-1][1]
    minimum_schedule = sorted_schedule[0][1]
    difference = maximum_schedule - minimum_schedule

    if 12 < difference:
        is_fair = False

if is_fair:
    print('Yes')
else:
    print('No')