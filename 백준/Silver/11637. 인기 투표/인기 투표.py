import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())

    total_vote = 0
    max_vote = 0
    max_vote_count = 0
    candidate_number = 0

    for i in range(1, n + 1):
        vote = int(sys.stdin.readline())

        total_vote += vote

        if max_vote == vote:
            max_vote_count += 1
            continue
        
        if max_vote < vote:
            max_vote = vote
            max_vote_count = 1
            candidate_number = i
            continue
        
    majority_count = (total_vote // 2) + 1

    if 1 < max_vote_count:
        print('no winner')
    elif majority_count <= max_vote:
        print(f'majority winner {candidate_number}')
    elif max_vote < majority_count:
        print(f'minority winner {candidate_number}')