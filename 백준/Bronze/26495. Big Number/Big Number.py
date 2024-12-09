line = input()

block_format_list = list(
    map(lambda x: x.split(),
        [
            '1111 1001 1001 1001 1111',
            '0001 0001 0001 0001 0001',
            '1111 0001 1111 1 1111',
            '1111 0001 1111 0001 1111',
            '1001 1001 1111 0001 0001',
            '1111 1 1111 0001 1111',
            '1111 1 1111 1001 1111',
            '1111 0001 0001 0001 0001',
            '1111 1001 1111 1001 1111',
            '1111 1001 1111 0001 0001'
        ])
)

for i, char in enumerate(line):
    index = int(char)

    for block_format in block_format_list[index]:
        print(''.join(map(lambda x: char if int(x) else ' ', block_format)))

    if i < len(line) - 1:
        print()