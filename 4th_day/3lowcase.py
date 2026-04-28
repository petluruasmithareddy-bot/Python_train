s1="CampusX is an Online Mentorship Program fOr EnginEering studentS"
upper_count=0
lower_count=0
for ch in s1:
    if ch.isupper():
        upper_count+=1
    elif ch.islower():
        lower_count+=1


print("uppercase",upper_count,)
print("lowercase",lower_count)
