nums=[2,3,4,3,2,1,2,2,1]
max={}
majority=0
value=0
for i in nums:
    if i not in max:
        max[i]=1
    else:
        max[i]+=1
    print(max)    
for key in max.keys():
    if max[key] > majority:
        majority=max[key]
        value=key
print(value)
print(max)
        