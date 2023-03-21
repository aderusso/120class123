a, b = 0, 1
sum_even = 0
while b < 4000000:
    # if the number is even, add it to sum_even
    if b % 2 == 0:
        sum_even += b
    # set a to b, and set b to a + b
    a, b = b, a+b

print(sum_even)

# answer should be 4613732
