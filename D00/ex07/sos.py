import sys

def data_dic(name):
    NESTED_MORSE = {'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ', 'E': '. ',
        'F': '..-. ', 'G': '--. ', 'H': '.... ', 'I': '.. ', 'J': '.--- ',
        'K': '-.- ', 'L': '.-.. ', 'M': '-- ', 'N': '-. ', 'O': '--- ',
        'P': '.--. ', 'Q': '--.- ', 'R': '.-. ', 'S': '... ', 'T': '- ',
        'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ',
        'Y': '-.-- ', 'Z': '--.. ',
        '0': '----- ', '1': '.---- ', '2': '..--- ', '3': '...-- ',
        '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ',
        '8': '---.. ', '9': '----. ',
        ' ': '/ '}
    for i in name:
        if not i.isspace():
            print(NESTED_MORSE[i.upper()],end='')
        else:
            print(NESTED_MORSE[i],end='')

    print()


def check_caractere(arg):
    for i in arg:
        assert i.isdigit() or i.isalpha() or i.isspace()
def main():
    assert len(sys.argv) == 2 ,"AssertionError: the arguments are bad"
    check_caractere(sys.argv[1])
    data_dic(sys.argv[1])

if __name__ == '__main__':
    main()