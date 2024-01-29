A, B, C = map(int, input().split())

parked_time = [0] * 101

for _ in range(3):
    arrive_time, leave_time = map(int, input().split())
    
    for i in range(arrive_time, leave_time):
        parked_time[i] += 1

total_fee = 0

total_fee += parked_time.count(1) * 1 * A
total_fee += parked_time.count(2) * 2 * B
total_fee += parked_time.count(3) * 3 * C

print(total_fee)