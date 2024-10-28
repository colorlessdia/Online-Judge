import sys

def calc_call_fee(record):
    call_fee = 10
    exceed_time = record - 100

    if exceed_time <= 0:
        return call_fee
    
    call_fee += (exceed_time // 50) * 3

    if exceed_time % 50 != 0:
        call_fee += 3
    
    return call_fee

n = int(sys.stdin.readline())

call_records = dict()

for _ in range(n):
    time, student = sys.stdin.readline().rstrip().split()

    hh, mm = map(int, time.split(':'))
    
    if student not in call_records:
        call_records[student] = 0

    call_records[student] += (hh * 60) + mm

record_list = []

for student, record in call_records.items():
    record_list.append((student, calc_call_fee(record)))

sorted_record_list = sorted(record_list, key=lambda x: (-x[1], x[0]))

for student, call_fee in sorted_record_list:
    print(student, call_fee)