import sys

def formatted_index(index):
    return int(index) - 1

C = int(sys.stdin.readline())

for customer_number in range(1, C + 1):
    print(f'Customer {customer_number}')

    security_questions = dict()

    A = int(sys.stdin.readline())

    for question_index in range(1, A + 1):
        word = ''.join(sys.stdin.readline().rstrip().split())

        security_questions[question_index] = word

    L = int(sys.stdin.readline())

    for _ in range(L):
        line = sys.stdin.readline().rstrip().split()

        word_index = int(line[0])
        blank_index_1, blank_index_2 = map(formatted_index, line[1:3])
        blank_char_1, blank_char_2 = line[3:]
    
        question = security_questions[word_index]

        if (
            question[blank_index_1] == blank_char_1 and
            question[blank_index_2] == blank_char_2
        ):
            print('correct')
        else:
            print('error')