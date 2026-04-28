num=[1,2,3,4,5,6,7,8,9]
# even_list = []
# for i in num:
#     if i % 2 ==0:
#         even_list.append(i)

# print(even_list)
even_list = [i for i in num if i%2 == 0]
print(even_list)