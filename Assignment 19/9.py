def palindrome_number():
    n=0
    while True:
        if str (n) ==str(n)[::-1]:
            yield n
        n +=1

gen = palindrome_number()
for _ in range(20):
    print(next(gen),end=" ")