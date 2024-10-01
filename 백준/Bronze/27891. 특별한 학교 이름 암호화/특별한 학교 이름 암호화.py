ciphertext = input()

school_names = {
    'NLCS': 'North London Collegiate School',
    'BHA': 'Branksome Hall Asia',
    'KIS': 'Korea International School',
    'SJA': 'St. Johnsbury Academy'
}

for k, v in school_names.items():
    temp = ''

    for c in v:
        
        if len(temp) == 10:
            break
        
        if not c.isalpha():
            continue
        
        if c.isupper():
            temp += c.lower()
            continue
        
        temp += c

    for i in range(26):
        formatted_name = ''

        for char in temp:
            char_code = ord(char) + i

            if ord('z') < char_code:
                char_code = (char_code % ord('z')) + ord('a') - 1
            
            formatted_name += chr(char_code)
        
        if formatted_name == ciphertext:
            print(k)
            break