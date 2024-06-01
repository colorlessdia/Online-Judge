import sys

time_record = dict()

A = int(sys.stdin.readline())

for _ in range(A):
    time = int(sys.stdin.readline())
    time_record[time] = 'A'

B = int(sys.stdin.readline())

for _ in range(B):
    time = int(sys.stdin.readline())
    time_record[time] = 'B'

sorted_time_record = sorted(time_record.items(), key=lambda x: x[0])

first_half = 0

A_score, B_score = 0, 0
count = 0
lead_team = ''

for record, team in sorted_time_record:
    if record <= 1440:
        first_half += 1

    if team == 'A':
        A_score += 1
    else:
        B_score += 1
    
    if lead_team == '':
        if B_score < A_score:
            lead_team = 'A'
        elif A_score < B_score:
            lead_team = 'B'
    elif lead_team == 'A':
        if A_score < B_score:
            count += 1
            lead_team = 'B'
    elif lead_team == 'B':
        if B_score < A_score:
            count += 1
            lead_team = 'A'

print(first_half)
print(count)