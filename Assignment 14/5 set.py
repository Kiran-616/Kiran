# Longest common prefix (using set)

strings = ["flower" , "flow" , "flight"]
prefix = ""

for i in range(len(min(strings,
key=len))):
    chars = {word[i] for word in strings}
    if len(chars) == 1:
        prefix += chars.pop()
    else:
        break
print("longest common prefix:" , prefix)
