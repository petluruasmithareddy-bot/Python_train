test_str = 'CampusX best for DS students.'
repl_dict = {"best": "is the best channel", "DS": "Data-Science"}

result = " ".join([repl_dict[word] if word in repl_dict else word 
                   for word in test_str.split()])

print(result)