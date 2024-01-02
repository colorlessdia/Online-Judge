t1, e1, f1 = map(int, input().split())
t2, e2, f2 = map(int, input().split())

max_time = (t1 * 3) + (e1 * 20) + (f1 * 120)
mel_time = (t2 * 3) + (e2 * 20) + (f2 * 120)

if max_time == mel_time:
    print('Draw')
elif mel_time < max_time:
    print('Max')
elif max_time < mel_time:
    print('Mel')