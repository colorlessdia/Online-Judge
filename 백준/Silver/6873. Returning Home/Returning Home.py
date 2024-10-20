import sys

route_history = []

while True:
    line = sys.stdin.readline().rstrip()

    if line == 'SCHOOL':
        break

    route_history.append(line)

direction = ''

for i, history in enumerate(route_history[::-1], 1):

    if history == 'L':
        direction = 'RIGHT'
        continue
    
    if history == 'R':
        direction = 'LEFT'
        continue

    print(f'Turn {direction} onto {history} street.')

    history = ''

print(f'Turn {direction} into your HOME.')