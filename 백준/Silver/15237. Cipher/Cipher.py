N, C = map(int, input().split())
frequency = list(map(int, input().split()))

number_history = dict()
length = 0

for number in frequency:

    if number not in number_history:
        number_history[number] = {
            'order': length,
            'count': 1
        }

        length += 1
        continue
    
    number_history[number]['count'] += 1

sorted_history = sorted(number_history.items(), 
                        key=lambda x: (-x[1]['count'], x[1]['order']))

print(' '.join([' '.join([str(k)] * v['count']) for k, v in sorted_history]))