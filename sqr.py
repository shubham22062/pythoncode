def sqrt_newton(number, tolerance=1e-10, max_iterations=1000):
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    
    guess = number / 2.0  # Initial guess
    
    for _ in range(max_iterations):
        new_guess = 0.5 * (guess + number / guess)
        if abs(new_guess - guess) < tolerance:
            return new_guess
        guess = new_guess
    
    return guess

# Example usage:
num = float(input("Enter a number to find its square root: "))
sqrt_value = sqrt_newton(num)
print(f"The square root of {num} is approximately {sqrt_value:.10f}")
