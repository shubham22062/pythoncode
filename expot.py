def exponentiation(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    
    # Handling negative exponents
    if exponent < 0:
        result = 1 / result
    
    return result

# Example usage:
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = exponentiation(base, exponent)
print(f"{base} raised to the power of {exponent} is {result:.10f}")
