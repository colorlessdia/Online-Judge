import sys

n = int(sys.stdin.readline())

matched_mission = {
    'HP': 103,
    'HS': 329,
    'HK': 466,
    'HT': 148,
    'PS': 408,
    'PK': 577,
    'PT': 260,
    'SK': 287,
    'ST': 226,
    'KT': 312
}

for i in range(1, n + 1):
    mission_string = 'H' + sys.stdin.readline().rstrip() + 'H'

    total_distance = 0

    for j in range(len(mission_string) - 1):
        mission = mission_string[j:j + 2]

        if mission not in matched_mission:
            mission = mission[::-1]

        total_distance += matched_mission[mission]

    print(f'Case {i}: {total_distance}')