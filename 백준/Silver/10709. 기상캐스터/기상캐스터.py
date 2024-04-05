import sys

H, W = map(int, sys.stdin.readline().split())

for _ in range(H):
    area_list = sys.stdin.readline().rstrip()

    cloud_list = [0] * W

    for i, area in enumerate(area_list):
        if i == 0 and area == '.':
            cloud_list[0] = -1
            continue

        if area == 'c':
            cloud_list[i] = 0
            continue

        if 'c' in area_list[:i]:
            cloud_list[i] = i - area_list[:i].rindex('c')
        else:
            cloud_list[i] = -1
    
    print(*cloud_list)