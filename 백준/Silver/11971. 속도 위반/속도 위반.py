N, M = map(int, input().split())

road_section = [0] * (100 + 1)
road_start = 1

for _ in range(N):
    road_end, road_speed = map(int, input().split())
    road_end += road_start - 1

    for i in range(road_start, road_end + 1):
        road_section[i] = road_speed
    
    road_start = road_end + 1

drive_section = [0] * (100 + 1)
drive_start = 1

for _ in range(M):
    drive_end, drive_speed = map(int, input().split())
    drive_end += drive_start - 1

    for j in range(drive_start, drive_end + 1):
        drive_section[j] = drive_speed
    
    drive_start = drive_end + 1

maximum_speed = 0

for road_speed, drive_speed in zip(road_section, drive_section):
    
    if drive_speed <= road_speed:
        continue
    
    if maximum_speed < drive_speed - road_speed:
        maximum_speed = drive_speed - road_speed

print(maximum_speed)