N = int(input())
number_list = list(map(int, input().split()))

odds = [number for number in number_list if number % 2 != 0]
evens = [number for number in number_list if number % 2 == 0]
group = set()
start = 0

if len(evens) < len(odds):
    group = set(odds)
    start = 1
else:
    group = set(evens)
    start = 2

while start in group:
    start += 2

print(start)