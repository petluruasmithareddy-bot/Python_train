test_dict = {"CampusX": [5, 7, 7, 7, 7], 
             "is": [6, 7, 7, 7], 
             "Best": [9, 9, 6, 5, 5]}

result = max(test_dict, key=lambda k: len(set(test_dict[k])))

print(result)