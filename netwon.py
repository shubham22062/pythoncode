def sqrt_newton_method(number, tolerance=1e-10, max_iterations=1000):
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    
    guess = number / 2.0  # Initial guess
    
    for _ in range(max_iterations):
        better_guess = 0.5 * (guess + number / guess)
        if abs(better_guess - guess) < tolerance:
            return better_guess
        guess = better_guess
    
    return guess

# Example usage:
num = 25
sqrt_value = sqrt_newton_method(num)
print(f"The square root of {num} is approximately {sqrt_value}")
