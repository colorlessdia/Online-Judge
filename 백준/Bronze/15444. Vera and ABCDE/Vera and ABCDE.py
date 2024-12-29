N = int(input())
S = input()

matched_code = {
    'A': ['***', '*.*', '***', '*.*', '*.*'],
    'B': ['***', '*.*', '***', '*.*', '***'],
    'C': ['***', '*..', '*..', '*..', '***'],
    'D': ['***', '*.*', '*.*', '*.*', '***'],
    'E': ['***', '*..', '***', '*..', '***'],
}

formatted_lines = [''] * 5

for char in S:
    
    for i, code in enumerate(matched_code[char]):
        formatted_lines[i] += code

for line in formatted_lines:
    print(line)