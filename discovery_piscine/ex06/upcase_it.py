many_words = input()
word = str(many_words.strip("'"))
word= str(word.strip('"'))
if word:
    print(word.upper())
else:
    print("none")