nm = int(input())

color = ''

if 620 <= nm:
    color = 'Red'
elif 590 <= nm:
    color = 'Orange'
elif 570 <= nm:
    color = 'Yellow'
elif 495 <= nm:
    color = 'Green'
elif 450 <= nm:
    color = 'Blue'
elif 425 <= nm:
    color = 'Indigo'
elif 380 <= nm:
    color = 'Violet'

print(color)