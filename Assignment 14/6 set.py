# Two numbers with max product
nums = [2,3,5,7,-1,4]
max_product = float("-inf")
max_pair = ()

 
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        product = nums[i] * nums[j]
        if product > max_product:
            max_product = product
            max_pair = (nums[i] , nums[j])

print("max product pair:" , max_pair , "product:" , max_product)