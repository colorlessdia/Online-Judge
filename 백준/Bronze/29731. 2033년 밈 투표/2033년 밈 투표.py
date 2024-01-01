promise_list = [
    'Never gonna give you up',
    'Never gonna let you down',
    'Never gonna run around and desert you',
    'Never gonna make you cry',
    'Never gonna say goodbye',
    'Never gonna tell a lie and hurt you',
    'Never gonna stop'
]

is_changed = 0

for _ in range(int(input())):
    s = input()

    if s not in promise_list:
        is_changed -= 1
        break

print('Yes') if is_changed < 0 else print('No')