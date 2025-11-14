import sys

input = sys.stdin.readline

T = 1

while True:
    N = int(input())

    if N == 0:
        break

    student_list = [0] * (N + 1)
    earring_dict = dict(zip(range(1, N + 1), [0] * N))

    for number in range(1, N + 1):
        name = input().rstrip()

        student_list[number] = name
    
    for _ in range((2 * N) - 1):
        number, _ = input().rstrip().split()
        number = int(number)

        earring_dict[number] += 1

        if earring_dict[number] == 2:
            del earring_dict[number]
    
    student_number = list(earring_dict.keys())[0]
    student_name = student_list[student_number]

    print(T, student_name)

    T += 1