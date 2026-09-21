many_words = input()
word = [str(i.strip('"')) for i in many_words.split('" "')]
print("Number of parameters:", len(word) if word[0] else 0)