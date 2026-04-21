my_list=['1ac21', '23fg', '456', '098d', '1', 'kls']

def get_product(my_list):
    product=1
    has_digits=False

    for ch in my_list:
        if ch.isdigit():
            product=product *int(ch)
            has_digits=True
    if has_digits:
        return product
    else:
        return 1
result=sorted(my_list,key=get_product,reverse=True)
print(result) 