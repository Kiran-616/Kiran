# Solve series
# 1. 1! + 2! + 3! + 4! +....+n!

n = int(input("Enter the value of n:"))

fact_sum = 0

def factorial(x):
    result = 1
    for i in range(1, n + 1):
        fact_sum += factorial(i)

print(f"Sum of factorial series : {fact_sum}")

# 2. series

n = int(input("Enter the value of N:"))
for i in range (1,n + 1):
    power_sum += n ** i

print(f"Sum of series N+N sq +...+N N {power_sum}")

# 3. series
n = int(input(" Enter number of terms:"))

a = 1
r = 2
sum_geo = 0
for i in range(n):
    sum_geo += a * (r ** i)
print(f"sum of geometric series: {sum_geo}")

# 4 . series

a = int(input("Enter value of a :"))
s = 0
for i in range (1 , 11):
    s+= (a ** i)/ i

print(f"sum of series s = a + a sq/2 + ....+ a 10/10: {s:2f}")

# 5. series

x = int(input("Enter the value of x :"))
n = int(input("Enter number of terms:"))

sum_series = 0
sign = 1
denominator = 1

for i in range (1,n+ 1):
    term = sign * (x ** i)/ denominator 

    sum_series += term
    sign *= -1
    denominator += 2

print(f"sum of the series : {sum_series} 2f")
