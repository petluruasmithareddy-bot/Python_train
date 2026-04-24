test_dict = {'c': [3], 'b': [12, 10], 'a': [19, 4]}

# sort keys + sort values
result = {k: sorted(v) for k, v in sorted(test_dict.items())}

print(result)