N = int(input())
S = input()

Adrian_list = ['A', 'B', 'C']
Bruno_list = ['B', 'A', 'B', 'C']
Goran_list = ['C', 'C', 'A', 'A', 'B', 'B']

score_dict = dict(zip(['Adrian', 'Bruno', 'Goran'], [0] * 3))

for i in range(N):
    answer = S[i]

    a = i % len(Adrian_list)
    b = i % len(Bruno_list)
    g = i % len(Goran_list)

    if answer == Adrian_list[a]:
        score_dict['Adrian'] += 1

    if answer == Bruno_list[b]:
        score_dict['Bruno'] += 1

    if answer == Goran_list[g]:
        score_dict['Goran'] += 1

maximum_score = max(score_dict.values())

print(maximum_score)

for id, score in score_dict.items():

    if score == maximum_score:
        print(id)