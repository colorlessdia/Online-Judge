N = int(input())
S = input()

grade_list = []
temp = []

for i in range(len(S) + 1):

    if i == len(S):

        if temp:
            grade_list.append(''.join(temp))

        break

    char = S[i]

    if char.isalpha():
        
        if not temp:
            temp.append(char)
            continue

        grade_list.append(''.join(temp))
        temp.clear()
        temp.append(char)
        continue

    temp.append(char)

converted_grade = []

A_2 = set(['A0', 'A'])
A123_B123 = set(['A+', 'A0', 'A', 'A-', 'B+', 'B0', 'B', 'B-'])
A3_B123_C123 = set(['A-', 'B+', 'B0', 'B', 'B-', 'C+', 'C0', 'C', 'C-'])
A3_B1 = set(['A-', 'B+'])
B23 = set(['B0', 'B', 'B-'])
B23_C123 = set(['B0', 'B', 'B-', 'C+', 'C0', 'C', 'C-'])
C123 = set(['C+', 'C0', 'C', 'C-'])

for i in range(N):
    grade = grade_list[i]
    is_first = (i == 0)
    before = None if is_first else grade_list[i - 1]

    if grade == 'A+':
        converted_grade.append('E')
    elif grade in A_2:
        
        if (i == 0) or (before in A3_B123_C123):
            converted_grade.append('E')
        else:
            converted_grade.append('P')

    elif grade in A3_B1:
        
        if (i == 0) or (before in B23_C123):
            converted_grade.append('P')
        else:
            converted_grade.append('D')

    elif grade in B23:
        
        if (i == 0) or (before in C123):
            converted_grade.append('D')
        else:
            converted_grade.append('B')

    elif grade in C123:
        converted_grade.append('B')

print(''.join(converted_grade))