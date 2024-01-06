def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(limit):
    prime_sum = 0
    for num in range(2, limit):
        if is_prime(num):
            prime_sum += num
    return prime_sum

n = 6
result = sum_of_primes(n)
print(f"The sum of prime numbers less than {n} is: {result}")

