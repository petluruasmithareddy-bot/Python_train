list1 = [1, 2, 3, 4, 5, 6]

result = []
total = 0

for num in list1:
    total += num        # add current number to total
    result.append(total)  # store the running sum

print(result)
