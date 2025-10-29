import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    K_set = set(map(int, input().split()))
    N = int(input())

    total_award = 0
    special_award = -1
    minimum_time = 361

    for _ in range(N):
        number, hour, minute = map(int, input().split())

        if hour == minute == -1:
            continue

        time = (hour * 60) + minute

        if (time <= 360) and (number in K_set):
            total_award += 1
            
            if time < minimum_time:
                special_award = number
                minimum_time = time

    print(special_award, total_award)