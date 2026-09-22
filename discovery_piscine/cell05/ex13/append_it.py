many_words = input()
word = [i.strip('"') for i in many_words.split('" "')]

if word[0]:
    for i in word:
        if not i.endswith("ism"):
            print(f"{i}ism")
else:
    print("none")