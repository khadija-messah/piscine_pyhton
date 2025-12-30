
from ft_filter import ft_filter

def check_caractere(c):
    if not c.isalpha():
        return 1
    return 0
def parssing_N(intiger):
    try:
        n = int(intiger)
    except ValueError:
        print("argument should be intiger")
        return 1

def parssing_S(s):
    try:
        s1 = str(s)
        arr = s.split()
        for i in arr:
            for s in i:
                assert check_caractere(s),"not caractere"
    except AssertionError as error:
        print(error)
        return 1
import sys
def filterstring():
    try:
        assert len(sys.argv) == 3 ,"error number argmuent"
        if parssing_N(sys.argv[2]):
            return
        if parssing_S(sys.argv[1]):
            return 
    except AssertionError as error:
        print(error)
filterstring()