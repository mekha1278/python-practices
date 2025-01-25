def remove(nums):
    n=len(nums)
    val=2
    left=0
    right=n-1
    while(left<=right):
        if nums[left]==val:
            nums.remove(nums[left])
            nums.append("_")
        else:
            left+=1
    print(nums)
nums=[0,1,2,2,3,0,4,2]
remove(nums)
