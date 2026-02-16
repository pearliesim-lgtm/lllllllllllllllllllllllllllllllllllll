set1={2,7,20,11}
set2={7,34,56,90}

print("set1=",set1)
print("set2=",set2)

u=set1.union(set2)
print("union=",u)

i=set1.intersection(set2)
print("Intersection=",i)

d=set1.difference(set2)
print("Difference=",d)

sd=set1.symmetric_difference(set2)
print("symmetric diffference=",sd)