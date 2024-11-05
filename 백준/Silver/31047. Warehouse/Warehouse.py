import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    toy_count = dict()

    for _ in range(N):
        toy, count = sys.stdin.readline().rstrip().split()
        count = int(count)

        if toy not in toy_count:
            toy_count[toy] = count
            continue
        
        toy_count[toy] += count
    
    print(len(toy_count))

    sorted_toy_count = sorted(toy_count.items(), key=lambda x: (-x[1], x[0]))
    
    for toy, count in sorted_toy_count:
        print(toy, count)