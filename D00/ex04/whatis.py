import sys

def main():
    if(len(sys.argv) == 1):
        return
    if(len(sys.argv) != 2):
        print("AssertionError: more than one argument is provided")
    else:
        try:
            intiger = int(sys.argv[1])
        except:
            print("AssertionError: argument is not an integer")
            return
        if(intiger % 2 == 0):
            print("I'm Even.")
        else:
            print("I'm Odd.")
if __name__ == '__main__':
    main()
else:
    print("you run in not curently")