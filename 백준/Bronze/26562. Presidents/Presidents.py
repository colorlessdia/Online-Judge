import sys

input = sys.stdin.readline

k = ['Franklin', 'Grant', 'Jackson', 'Hamilton', 'Lincoln', 'Washington']
v = [100, 50, 20, 10, 5, 1]
matched_count = dict(zip(k, v))

N =  int(input())

for _ in range(N):
    president_list = input().rstrip().split()

    count = 0

    for president in president_list:
        count += matched_count[president]
    
    print(f'${count}')