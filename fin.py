def fibonacci_series(n):
    series = []
    a, b = 0, 1
    while len(series) < n:
        series.append(a)
        a, b = b, a + b
    return series

# Example usage:
num_terms = int(input("Enter the number of terms in the Fibonacci series: "))
fib_series = fibonacci_series(num_terms)
print("Fibonacci series:", fib_series)
