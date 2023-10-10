import sys

while 1:
    w = sys.stdin.readline().rstrip()
    
    if w == '#':
        break
      
    break_index = -1
    is_find = False
    
    for i, ww in enumerate(w):
        if ww in list('aeiou'):
            if i == 0:
                print(w + 'ay')
                is_find = True
            else:
                break_index = i
                
            break
    if not is_find:
        if break_index == -1:
            print(w + 'ay')
        else:
            print(w[break_index:] + w[:break_index] + 'ay')