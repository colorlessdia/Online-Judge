N = int(input())

time = 0

while 0 < N:
    K = 1
    
    while K <= N:
        N -= K
        K += 1
        time += 1

print(time)