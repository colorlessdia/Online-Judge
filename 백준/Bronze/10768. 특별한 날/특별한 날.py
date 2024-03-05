month = int(input())
date = int(input())

if month == 2 and date == 18:
    print('Special')
elif (month == 2 and date < 18) or month < 2:
    print('Before')
else:
    print('After')