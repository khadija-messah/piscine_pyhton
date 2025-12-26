import sys

def main():
    if(len(sys.argv) < 2):
        exit()
    if(len(sys.argv) != 2):
        print("AssertionError: more than one argument is provided")
    else:
        try:
            intiger = int(sys.argv[1])
            if(isinstance(intiger,int)):
                if(intiger % 2 == 0):
                    print("I'm Even.")
                else:
                    print("I'm Odd")
        except:
            print("AssertionError: argument is not an integer")
main()