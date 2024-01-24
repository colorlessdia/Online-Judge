import sys

T = int(input())

matched_gandalf_score = [1, 2, 3, 3, 4, 10]
matched_sauron_score = [1, 2, 2, 2, 3, 5, 10]

for case in range(1, T + 1):
    gandalf = list(map(int, sys.stdin.readline().split()))
    sauron = list(map(int, sys.stdin.readline().split()))

    gandalf_score = sum([matched_gandalf_score[i] * tribe for i, tribe in enumerate(gandalf)])
    sauron_score = sum([matched_sauron_score[i] * tribe for i, tribe in enumerate(sauron)])

    if gandalf_score == sauron_score:
        print(f'Battle {case}: No victor on this battle field')
    elif sauron_score < gandalf_score:
        print(f'Battle {case}: Good triumphs over Evil')
    elif gandalf_score < sauron_score:
        print(f'Battle {case}: Evil eradicates all trace of Good')