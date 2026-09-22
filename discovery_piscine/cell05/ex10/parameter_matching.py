import sys

if len(sys.argv) == 2:
    text_input = input("What was the parameter? ")
    if sys.argv[1] == text_input:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")
