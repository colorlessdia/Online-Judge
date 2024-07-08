yut_list = [str(sum(map(int, input().split()))) for _ in range(3)]

matched_yut = dict(zip(list('32104'), list('ABCDE')))

for yut in yut_list:
    print(matched_yut[yut])