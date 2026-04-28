string=["I Love India","I Love food"]
final={}
for sentence in string:
    for word in sentence.split():
       if word not in final:
           final[word]=1
       else:
           final[word]+=1

print(final)