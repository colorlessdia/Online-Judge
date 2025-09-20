import sys

def time_to_minute(time):
    hh, mm = map(int, time.split(':'))

    return (hh * 60) + mm

input = sys.stdin.readline

S, E, Q = map(time_to_minute, input().rstrip().split())

check_history = dict()

while True:
    line = input().rstrip().split()

    if len(line) == 0:
        break

    time = time_to_minute(line[0])
    id = line[1]

    if time <= S:
        check_history[id] = False
        continue

    if E <= time <= Q:
        
        if id in check_history:
            check_history[id] = True

count = 0

for v in check_history.values():
    
    if v:
        count += 1

print(count)