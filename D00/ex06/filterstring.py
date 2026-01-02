
import sys
from ft_filter import ft_filter
def main():
    try:
        assert len(sys.argv) == 3
        assert sys.argv[2].isdigit()
        
        s = int(sys.argv[2])
        res = sys.argv[1]
        words = res.split()
        li = list(ft_filter(lambda name : len(name) > s, words))
        print(li)
    except AssertionError as error:
        print("AssertionError: the arguments are bad")

if __name__ == "__main__":
    main()