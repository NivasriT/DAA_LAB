print("NIVASRI T | 24BAD081")
import time

# Iterative Fibonacci Function
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

# Recursive Factorial Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Main Program
values = [10, 20, 30, 40]

for n in values:
    # Measure Fibonacci time
    start = time.time()
    fib_result = fibonacci(n)
    fib_time = time.time() - start

    # Measure Factorial time
    start = time.time()
    fact_result = factorial(n)
    fact_time = time.time() - start

    print("n =", n)
    print("Fibonacci:", fib_result, "| Time:", fib_time)
    print("Factorial:", fact_result, "| Time:", fact_time)
    print("--")
