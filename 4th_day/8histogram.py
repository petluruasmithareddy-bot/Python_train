n=[13,42,15,37,22,39,41,50]
final={}
for num in n:
    if num in range(11,21):
        if "11-20" not in final:
            final["11-20"]=1
        else:
            final["11-20"]+=1
    elif num in range(21,31):
            if "21-30 "not in final:
                 final["21-30"]=1
            else: 
                 final["21-30"]+=1
    elif num in range(31,41):
         if "31-40" not in final:
              final["31-40"]=1
         else:
              final["31-40"]+=1
    elif num in range(41,51):
         if "41-50" not in final:
              final["41-50"]=1
         else:
              final["41-50"]+=1
print(dict(sorted(final.items())))  #dict-for converting list of tuples-dict,.items-to both both keys and values in dictionary format
         
        