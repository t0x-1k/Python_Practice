def fibonacci_iterative(n):
    fib_sequence = [0, 1]
    for i in range(2, n+1):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence[n]

# Example usage:
result = fibonacci_iterative(8)
print(result)
