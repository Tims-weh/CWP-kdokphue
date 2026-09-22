word = input().strip('"')
if not word:
    print("none")
else:
    text_input = str(input("What was the parameter? "))
    if word == text_input:
        print("Good job!")
    else:
            print("Nope, sorry...")