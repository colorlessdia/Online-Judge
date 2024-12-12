import sys

monument_dict = dict()
monument_count = 0

while True:
    line = sys.stdin.readline().rstrip()

    if line == '':
        break
    
    date_length = len('YYYY-MM-DD')
    
    date, monument = line[:date_length], line[date_length + 1:]

    if monument not in monument_dict:
        monument_dict[monument] = 1
        monument_count += 1

print(monument_count)