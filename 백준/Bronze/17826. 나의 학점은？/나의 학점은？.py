score_list = list(map(int, input().split()))
score = int(input())

rank = score_list.index(score) + 1

if 49 <= rank <= 50:
    print('F')
elif 46 <= rank <= 48:
    print('C0')
elif 36 <= rank <= 45:
    print('C+')
elif 31 <= rank <= 35:
    print('B0')
elif 16 <= rank <= 30:
    print('B+')
elif 6 <= rank <= 15:
    print('A0')
elif 1 <= rank <= 5:
    print('A+')