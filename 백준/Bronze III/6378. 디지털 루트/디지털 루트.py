import sys

while True:
    number = sys.stdin.readline().rstrip()

    if number == '0':
        break
    
    while 1 < len(number):
        number = str(sum(map(int, list(number))))
    
    print(number)