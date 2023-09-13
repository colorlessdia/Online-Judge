depth = [int(input()) for _ in range(4)]

d = 0

for i in range(3):
    if depth[i + 1] > depth[i]:
        d += 1
    elif depth[i + 1] < depth[i]:
        d -= 1

if len(set(depth)) == 1: 
    print('Fish At Constant Depth')
elif d == 3:
    print('Fish Rising')
elif d == -3:    
    print('Fish Diving')
else:
    print('No Fish')