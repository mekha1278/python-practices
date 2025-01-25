nums=[1,2,3,4,5,6,7,8,9,10]
target=8
n=len(nums)
left=0
right=n-1
while(left<=right):
    mid=(left+right)//2
    if nums[mid]==target:
        print(mid) 
        break  
    elif nums[mid]<target:
        left=mid+1
    elif nums[mid]>target:
        right=mid-1
        

