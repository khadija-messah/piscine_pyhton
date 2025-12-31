
import sys
from ft_filter import ft_filter

def check_caractere(c):
    if not c.isalpha():
        return 0
    return 1
def parssing_N(intiger):
    try:
        n = int(intiger)
    except ValueError:
        print("AssertionError: argument should be intiger")
        return 1

def parssing_S(s):
    result = []
    try:
        s1 = str(s)
        arr = s.split()
        for i in arr:
            for s in i:
                assert check_caractere(s),"not caractere"
            result.append(i)
    except AssertionError as error:
        print(error)
        return 1
    return result

def filterstring():
    try:
        assert len(sys.argv) == 3 ,"AssertionError: error number argmuent"
        if parssing_N(sys.argv[2]):
            return
        s = int(sys.argv[2])
        res = parssing_S(sys.argv[1])
        t = []
        if res == 1:
            return
        li = print(list(ft_filter(lambda name : len(name) > s, res)))
    except AssertionError as error:
        print(error)
filterstring()
print(ft_filter.__doc__)