import sys

input = sys.stdin.readline

N, M = map(int, input().split())
bus_schedule = list(map(int, input().split()))

destination_dict = dict()

for i in range(len(bus_schedule) - 1):
    origin = bus_schedule[i]
    destination = bus_schedule[i + 1]

    destination_dict[origin] = destination

total_transfer_fee = 0

for bus_number in range(1, N + 1):
    transfer_fee_list = [0] + list(map(int, input().split()))

    if bus_number not in destination_dict:
        continue
    
    index = destination_dict[bus_number]
    total_transfer_fee += transfer_fee_list[index]

    del destination_dict[bus_number]

print(total_transfer_fee)