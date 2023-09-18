import sys

char_dict = dict(zip([' ', '!', '$', '%', '(', ')', '*'], ('%20 %21 %24 %25 %28 %29 %2a').split()))

while 1:
    s = sys.stdin.readline().rstrip()
    
    if s == '#': break
    
    encoding_string = ''
    
    for ss in s:
        if ss in char_dict:
            encoding_string += char_dict[ss]
        else:
            encoding_string += ss
    
    print(encoding_string)