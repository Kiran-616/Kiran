#  Missing coin number

nums = list(map(int,input("enter coin numbers:") .split()))

missing = 0
for n in nums:
    missing ^= n
print("missing coin number:" , missing)

