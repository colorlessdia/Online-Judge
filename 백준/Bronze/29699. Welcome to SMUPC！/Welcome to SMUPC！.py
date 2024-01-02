n = int(input()) - 1
s = 'WelcomeToSMUPC'

if n < len(s):
    print(s[n])
else:
    print(s[n % len(s)])