
from ft_filter import ft_filter


def parssing_N(intiger):
    try:
        n = int(intiger)
    except ValueError:
        print("argument should be intiger")
        return 1
import sys
def filterstring():
    try:
        assert len(sys.argv) == 3 ,"error number argmuent"
        if parssing_N(sys.argv[2]):
            return
    except AssertionError as error:
        print(error)
filterstring()