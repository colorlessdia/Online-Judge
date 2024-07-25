import sys

n, m = map(int, input().split())

survey_count = dict(zip(range(1, m + 1), [0] * m))

for _ in range(n):
    survey_list = list(map(int, sys.stdin.readline().split()))

    for i, survey in enumerate(survey_list, 1):
        if survey:
            survey_count[i] += 1

sorted_survey = sorted(survey_count.items(), key=lambda x: (-x[1], x[0]))

for i, survey in enumerate(sorted_survey, 1):
    if i == m:
        print(survey[0], end='')
    else:
        print(survey[0], end=' ')