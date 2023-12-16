import sys

matched_dict = dict(zip(['Algorithm', 'DataAnalysis', 'ArtificialIntelligence', 'CyberSecurity', 'Network', 'Startup', 'TestStrategy'], ['204', '207', '302', 'B101', '303', '501', '105']))

for _ in range(int(input())):
    seminar = sys.stdin.readline().rstrip()

    print(matched_dict[seminar])