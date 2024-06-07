import sys

while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break
    
    height_dict = dict()
    
    for _ in range(N):
        name, height = sys.stdin.readline().rstrip().split()

        height = int(float(height) * 100)

        if height in height_dict:
            height_dict[height] += [name]
        else:
            height_dict[height] = [name]

    max_height = max(height_dict.keys())

    print(*height_dict[max_height])