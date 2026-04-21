data = ['campusxIs', 'bestFor', 'dataScientist']

result = []

for word in data:
    new_word = ""
    for ch in word:
        if ch.isupper():        # check uppercase
            new_word += " " + ch
        else:
            new_word += ch
    result.append(new_word)

print(result)