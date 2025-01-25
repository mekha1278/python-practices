def majority_elements(nums):
    max_num=max(nums)
    number=[0]*(max_num+1)
    print(number)
    for i in nums:
        number[i]+=1
    majority=0
    high=0
    for i in range(1,max_num+1):
        if(number[i]>high):
            majority=i
            high=number[i]
        print(f"number[{i}={number[i]}")    
    print(majority)
majority_elements([1,2,1,2,2,3,4,4,5,6])
majority_elements([1,2,1,2,1,2,4,4,3,4,4,5,6])
