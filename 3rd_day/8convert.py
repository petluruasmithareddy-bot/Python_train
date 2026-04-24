test_list = ["DataScience", 3, "is", 8]
key_list = ["name", "id"]
n=len(key_list)
result=[]
for i in range (0,len(test_list),n):
    slice_list=test_list[i:i+n]
    result.append(dict(zip(key_list,slice_list))) 
print(result)