data = [("akash", 10), ("gaurav", 12), ("anand", 14), 
        ("suraj", 20), ("akhil", 25), ("ashish", 30)]

result={}
for key,value in data:
    if key not in result:
        result[key]=[value]
    else:
        result[key].append(value)

print(result)