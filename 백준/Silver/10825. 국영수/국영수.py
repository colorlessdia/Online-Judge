import sys

N = int(sys.stdin.readline())

student_list = [sys.stdin.readline().rstrip().split() for _ in range(N)]

for student in sorted(student_list, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])):
    print(student[0])