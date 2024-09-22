m = int(input())
A_course = input().split()

completed_course = dict()

for course in A_course:
    completed_course[course] = 1

n = int(input())
B_course = input().split()

is_included = True

for course in B_course:
    
    if course not in completed_course:
        is_included = False
        break

if is_included:
    print(1)
else:
    print(0)