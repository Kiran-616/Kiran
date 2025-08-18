# Frequency dictionary

lst = [1,3,4,1,2,3,6,7,1,2,4]
freq = {}

for num in lst:
    freq[num] = freq.get(num,0 ) + 1

print(freq)