N = input()

initial_number = N

if len(N) < 2:
    initial_number = '0' + N

cycle = 0

while True:
    if len(N) < 2:
        N = '0' + N
    
    front_number = N[-1]
    back_number = str(int(N[0]) + int(N[-1]))[-1]

    N = front_number + back_number

    cycle += 1

    if initial_number == N:
        break

print(cycle)