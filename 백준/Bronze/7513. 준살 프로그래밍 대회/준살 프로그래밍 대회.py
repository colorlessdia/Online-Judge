import sys

t = int(input())

for i in range(1, t + 1):
    print(f'Scenario #{i}:')

    m = int(sys.stdin.readline())

    word_list = [sys.stdin.readline().rstrip() for _ in range(m)]
    
    n = int(sys.stdin.readline())

    for _ in range(n):
        password_info = list(map(int, sys.stdin.readline().split()))

        password = ''

        for index in password_info[1:]:
            password += word_list[index]
        
        print(password)
    
    print()