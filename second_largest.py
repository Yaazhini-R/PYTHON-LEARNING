nums = [10, 5, 20, 8, 15]
largest = nums[0]
seclargest = nums[0]
for i in range(len(nums)):
    if(nums[i]>largest):
        seclargest=largest
        largest=nums[i]
    elif(nums[i]<largest and nums[i]>seclargest):
        seclargest=nums[i]
print(seclargest)
