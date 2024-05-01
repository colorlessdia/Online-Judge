import sys

def custom_round(number):
    if 0.5 <= number - int(number):
        return int(number) + 1
    
    return int(number)

n = int(sys.stdin.readline())

if n == 0:
    print(n)
else:
    difficulty_list = sorted([int(sys.stdin.readline()) for _ in range(n)])

    exception = custom_round(n * 0.15)

    if exception != 0:
        difficulty_list = difficulty_list[exception:-exception]
    
    divisor = n - (exception * 2)

    print(custom_round(sum(difficulty_list) / divisor))