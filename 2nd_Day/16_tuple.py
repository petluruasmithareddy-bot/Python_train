list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
result={}


for a, b in test_list:
    if a not in result:
        result[a] = [b]
    else:
        result[a].append(b)

# print(result)

final = []
for key in result:
    final.append((key, *result[key]))

print(final)