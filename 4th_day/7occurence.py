n="hello how are you i am fine thank you"
words = n.split()
words_count = {}
for each_word in words:
    if each_word not in words_count:
        words_count[each_word] = 1
    else:
        words_count[each_word] +=1
 
required_key = max(words_count)      
print(f"{required_key} - {words_count[required_key]}")