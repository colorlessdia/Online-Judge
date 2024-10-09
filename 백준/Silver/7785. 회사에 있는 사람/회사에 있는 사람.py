import sys

n = int(sys.stdin.readline())

company_state = dict()

for _ in range(n):
    name, state = sys.stdin.readline().rstrip().split()

    if name not in company_state:
        company_state[name] = state
        continue
    
    if company_state[name] == 'enter':
        del company_state[name]

sorted_company_state = sorted(company_state.keys(), reverse=True)

for name in sorted_company_state:
    print(name)