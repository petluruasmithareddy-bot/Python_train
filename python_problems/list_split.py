data = ['CampusX is a channel', 'for data-science', 'aspirants.']

result = []

for sentence in data:
    words =sentence.split(' ')   # split by space
    result.extend(words)          # add words to result list

print(result)