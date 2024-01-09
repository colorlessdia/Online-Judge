import sys

n = int(sys.stdin.readline())

def factorial(n):
    if n == 1 or n == 0:
        return 1
    elif n >= 2:
        return n * factorial(n - 1)
    
print(factorial(n))