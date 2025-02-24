# Task 1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(4))
print(is_prime(7))

# Task 2
def digit_sum(k):
        if k == 0:
         return 0
        return k % 10 + digit_sum(k//10)
print(digit_sum(24))
print(digit_sum(502))

# Task 3
def powers_of_two(N):
    k = 2
    while k <= N:
        print(k, end =" ")
        k *= 2
powers_of_two(10)
            
     

