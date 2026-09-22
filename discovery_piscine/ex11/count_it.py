many_words = input()
word = [i.strip('"') for i in many_words.split('" "')]

if word[0]:
    print("parameters:", len(word))
    for i in word:
        print(f"{i}: {len(i)}")
else:
    print("none")