# All pairs whose sum is given

nums = [2,4,3,5,6,-2,4,7,8,9]
target_sum = 7
pairs = set()

for i in range(len (nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target_sum:
            pairs.add((nums[i] , nums[j]))

print("pairs with sum" , target_sum , ":" ,pairs)
