def is_CPP(var):
    
    if var[0] == '_' or var[-1] == '_':
        return 0
    
    for i, char in enumerate(var):
        
        if char.isupper():
            return 0
        
        if i == 0:
            continue
        
        if var[i - 1] + char == '__':
            return 0
    
    return 1

def is_Java(var):
    
    if var[0].isupper():
        return 0
    
    if '_' in var:
        return 0

    return 1

def CPP_to_Java(cpp):
    java = ''
    
    for i, char in enumerate(cpp):
        
        if char == '_':
            continue
        
        if cpp[i - 1] == '_':
            java += char.upper()
            continue
        
        java += char
    
    return java

def Java_to_CPP(java):
    cpp = ''

    for char in java:
        
        if char.isupper():
            cpp += '_' + char.lower()
            continue
        
        cpp += char

    return cpp

s = input()

if is_Java(s) and is_CPP(s):
    print(s)
elif is_Java(s):
    print(Java_to_CPP(s))
elif is_CPP(s):
    print(CPP_to_Java(s))
else:
    print('Error!')