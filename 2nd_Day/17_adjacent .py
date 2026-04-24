t=(1,5,7,8,10)
result=tuple(
    t[i]*t[i+1] if i ==0 else
    t[i]*t[i-1]+t[i]*t[i+1] if i < len(t)-1 else
    t[i]*t[i-1]
    for i in range (len(t)))
print(result)