list1 = [2, 4, 6, 10, 1]

result = []

for i in range(len(list1)):
    total = 0
    for j in range(len(list1)):
        if list1[j] > list1[i]:   # check for greater elements
            total += list1[j]
    total += list1[i]  # add the element itself
    result.append(total)

print(result)