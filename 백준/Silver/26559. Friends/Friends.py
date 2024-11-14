import sys

n = int(sys.stdin.readline())

for _ in range(n):
    m = int(sys.stdin.readline())

    friends = dict()

    for _ in range(m):
        name, num = sys.stdin.readline().rstrip().split()
        num = int(num)

        friends[name] = num
    
    sorted_friends = sorted(friends.items(), key=lambda x: -x[1])

    formatted_friends = ', '.join([sorted_friends[i][0] for i in range(m)])

    print(formatted_friends)