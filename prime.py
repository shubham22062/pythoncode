def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def find_n_primes(n):
    primes = []
    num = 2  # Start checking for primes from 2
    
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    
    return primes

# Example usage:
n = int(input("Enter the number of prime numbers to find: "))
prime_numbers = find_n_primes(n)
print(f"The first {n} prime numbers are: {prime_numbers}")
