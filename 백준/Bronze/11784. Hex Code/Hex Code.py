import sys

matched_ascii = dict()

for i in range(10, 127 + 1):
    matched_ascii[hex(i)[2:]] = chr(i)

while True:
    hex_code = sys.stdin.readline().rstrip().lower()

    if hex_code == '':
        break
    
    decoded_text = ''

    for i in range(0, len(hex_code), 2):
        decoded_text += matched_ascii[hex_code[i:i + 2]]
    
    print(decoded_text)