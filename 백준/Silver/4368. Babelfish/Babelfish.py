import sys

dictionary = dict()

while True:
    line = sys.stdin.readline().rstrip()

    if line == '':
        break
    
    original_text, translated_text = line.split()

    dictionary[translated_text] = original_text
    
while True:
    word = sys.stdin.readline().rstrip()

    if word == '':
        break
    
    if word in dictionary:
        print(dictionary[word])
    else:
        print('eh')