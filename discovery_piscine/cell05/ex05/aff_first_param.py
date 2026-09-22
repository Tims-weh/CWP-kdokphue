many_words = input()
word = [str(i.strip('"')) for i in many_words.split('" "')]
print(word[0] if word[0] else "none")