nums=[1,1,2,3,3,4,5]
k=1

for i in range(len(nums)-1,0,-1):
    print(i,nums[i])
    if nums[i]==nums[i-1]:
        nums.pop(i)




##for i in range(1,len(nums)):
##    print(nums[k],k,nums[i],i)
##    if nums[i] != nums[i-1]:
##        nums[k]=nums[i]
##        k+=1


print(nums,k)
        
