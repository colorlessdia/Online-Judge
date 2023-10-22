import sys

a = 'CU :-) :-( ;-) :-P (~.~) TA CCC CUZ TY YW TTYL'.split()
b = 'see you,I’m happy,I’m unhappy,wink,stick out my tongue,sleepy,totally awesome,Canadian Computing Competition,because,thank-you,you’re welcome,talk to you later'.split(',')

matched_dict = dict(zip(a, b))

while 1:
    s = sys.stdin.readline().rstrip()
    
    if s in matched_dict:
        print(matched_dict[s])
    else:
        print(s)
    
    if s == 'TTYL':
        break