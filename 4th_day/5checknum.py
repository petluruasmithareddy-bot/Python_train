num=int(input("enter the number:"))
total=0
for i in range(1,num):
    if num%i==0:
        total+=i
if total==num:
    print("perfectnumber")
else:
    print("notperfect")