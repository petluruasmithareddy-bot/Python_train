import math
co_list=[(1,1),(2,2),(3,3),(4,4)]
x,y=map(int,input("enter query points").split())
closest_distance={}
u=(x,y)
for num in co_list:
    distance=math.sqrt((num[0]-u[0]**2)+(num[1]-u[1]**2))
    closest_distance[num]=distance
print(min(closest_distance,key=closest_distance.get))