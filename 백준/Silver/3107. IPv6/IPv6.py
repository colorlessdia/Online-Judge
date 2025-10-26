IP = input()
IPv6 = IP

if '::' in IP:
    F, B = IP.split('::')

    group_count = 0

    if F:
        group_count += len(F.split(':'))
    
    if B:
        group_count += len(B.split(':'))
    
    zero_string = ':0000' * (8 - group_count)

    if (not F) and (not B):
        IPv6 = '0000' + zero_string
    elif not F:
        IPv6 = zero_string[1:] + ':' + B
    elif not B:
        IPv6 = F + zero_string
    else:
        IPv6 = F + zero_string + ':' + B

IPv6 = ':'.join(map(lambda x: x.zfill(4), IPv6.split(':')))

print(IPv6)