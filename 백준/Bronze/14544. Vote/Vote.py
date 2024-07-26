import sys

P = int(sys.stdin.readline())

for case_count in range(1, P + 1):
    n, m = map(int, sys.stdin.readline().split())

    vote_count = {sys.stdin.readline().rstrip(): 0 for _ in range(n)}

    for _ in range(m):
        X, R, C = sys.stdin.readline().rstrip().split()

        vote_count[X] += int(R)

    sorted_vote = sorted(vote_count.items(), key=lambda x: -x[1])

    if sorted_vote[0][1] == sorted_vote[1][1]:
        print(f'VOTE {case_count}: THERE IS A DILEMMA')
    else:
        print(f'VOTE {case_count}: THE WINNER IS {sorted_vote[0][0]} {sorted_vote[0][1]}')