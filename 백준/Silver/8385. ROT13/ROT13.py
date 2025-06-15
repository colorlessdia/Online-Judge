import sys

def ROT13(word, table):
    return ''.join([table[char] for char in word])

input = sys.stdin.readline

conversion_table = dict()

for i in range(ord('a'), ord('z') + 1):
    j = i + 13

    if ord('z') < j:
        j = ord('a') + (j % ord('z')) - 1
    
    conversion_table[chr(i)] = chr(j)

N = int(input())

word_count = dict()
except_word = dict()

count = 0

for _ in range(N):
    word = input().rstrip()

    if word in except_word:
        continue

    converted_word = ROT13(word, conversion_table)

    if converted_word not in word_count:
        word_count[word] = 1
        continue
    
    except_word[word] = 1
    except_word[converted_word] = 1

    count += 2

print(count)