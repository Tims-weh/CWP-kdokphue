many_words = input()
word = [str(i.strip('"')) for i in many_words.split('" "')]
if len(word) < 2:
    print("none")    
else:
    for i in word:
        print(i)