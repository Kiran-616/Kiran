# unique combinations of 3 numbers with given sum
nums = [1,2,3,4,5,6]
target = 10
combinations = set()

for i in range(len(nums)):
    for j in range(i+1 , len(nums)):
        for k in range(j+1, len(nums)):
            if nums [i]+ nums[j]+ nums[k] == target:
                combinations.add(tuple(sorted([nums[i],nums[j],nums[k]])))
            


print("combinations summing to" , target, ":" , combinations)
