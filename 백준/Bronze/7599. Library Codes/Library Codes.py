import sys

while True:
    library, font = sys.stdin.readline().rstrip().split()

    font = int(font)

    if library == '#' and font == 0:
        break
    
    print(f'{library} Library')
    
    count = int(sys.stdin.readline())

    for n in range(1, count + 1):
        width, text = sys.stdin.readline().rstrip().split()

        width = int(width)
        length = len(text)
        gap = 2

        label_width = (length * font) + gap

        direction = 'vertical' if width < label_width else 'horizontal'

        print(f'Book {n} {direction}')