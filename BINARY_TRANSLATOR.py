binary_translator = {
    'a': '01000001',
    'b': '01000010',
    'c': '01000011',
    'd': '01000100',
    'e': '01000101',
    'f': '01000110',
    'g': '01000111',
    'h': '01001000',
    'i': '01001001',
    'j': '01001010',
    'k': '01001011',
    'l': '01001100',
    'm': '01001101',
    'n': '01001110',
    'o': '01001111',
    'p': '01010000',
    'q': '01010001',
    'r': '01010010',
    's': '01010011',
    't': '01010100',
    'u': '01010101',
    'v': '01010110',
    'w': '01010111',
    'x': '01011000',
    'y': '01011001',
    'z': '01011010',
    ' ': '00100000',
    ',': '00101100',
    '.': '00101110'
}

your_string = input(str('type in your name here')).lower()

print(f'YOUR STRING: {your_string}')
print('\nyour binary translation:\n')

for single in your_string:
    for key, value in binary_translator.items():
        if single in key:
#            print(f'LETTER-{key.upper()}, BINARY-{value}')
            print(value, end=' ')


