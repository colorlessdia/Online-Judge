while True:

    try:
        word_list = input().split()

        vowel_list = []
        vowel_index_list = []

        for i, word in enumerate(word_list):
            
            if word[0] in 'aeiouAEIOU':
                vowel_list.append(word)
                vowel_index_list.append(i)

        for index, vowel in zip(vowel_index_list[::-1], vowel_list):
            word_list[index] = vowel
        
        reversed_sentence = ' '.join(word_list)

        print(reversed_sentence)
    except:
        break