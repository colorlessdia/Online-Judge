start_hour, start_minute = map(int, input().split())
end_hour, end_minute = map(int, input().split())
N = input()

count = 0

while True:
    if (N in str(start_hour).zfill(2)) or (N in str(start_minute).zfill(2)):
        count += 1

    if (start_hour == end_hour) and (start_minute == end_minute):
        break

    start_minute += 1

    if 59 < start_minute:
        start_hour += 1
        start_minute = 0
    
    if 23 < start_hour:
        break

print(count)