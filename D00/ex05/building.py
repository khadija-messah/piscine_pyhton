import sys

def calcu(line):
    characters = 0
    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
    digits = 0
    s = len(line)
    for i in line:
        if i.isdigit():
            digits+=1
        elif i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        elif i.isspace():
            spaces+=1
        else:
            punctuation+=1
    print(f"The text contains {s} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")
    return

def main():
    if len(sys.argv) > 2:
        print("AssertionError")
        return
    if len(sys.argv) == 1:
        line = sys.stdin.read()
    else:
        line = sys.argv[1]
    calcu(line)

if __name__ == "__main__":
    main()