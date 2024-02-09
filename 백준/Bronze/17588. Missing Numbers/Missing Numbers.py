import sys

n = int(input())

number_list = [int(sys.stdin.readline()) for _ in range(n)]

if len(number_list) == number_list[-1]:
    print('good job')
else:
    for i in range(1, number_list[-1] + 1):
        if i not in number_list:
            print(i)