import sys

T = int(input())

for _ in range(T):
    J = int(sys.stdin.readline())

    for i in range(1, J + 1):
        if i == 1 or i == J:
            print('#' * J)
        else:
            print('#' + ('J' * (J - 2)) + '#')
    
    print()