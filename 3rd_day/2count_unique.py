Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
vowels="aeiouAEIOU"
unique_vowels=set()
for ch in Str1:
    if ch in vowels:
        unique_vowels.add(ch)
print("no of unique_vowels-",len(unique_vowels))