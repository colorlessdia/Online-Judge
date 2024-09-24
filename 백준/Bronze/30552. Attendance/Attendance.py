import sys

N = int(sys.stdin.readline())

student = ''
absence_list = []

for _ in range(N):
    line = sys.stdin.readline().rstrip()

    if line == 'Present!':
        student = ''
        continue
    
    if student != '':
        absence_list.append(student)

    student = line

if student != '':
    absence_list.append(student)

if len(absence_list) == 0:
    print('No Absences')
else:
    
    for absence_student in absence_list:
        print(absence_student)