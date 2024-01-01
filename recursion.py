# fibonacci
def fibonacci(n):
    if n in [0, 1]: return n
    return fibonacci(n-2) + fibonacci(n-1)

n = fibonacci(6)
print(n)

# factorial
def factorial(n):
    if n <= 0: return 0
    if n == 1: return 1
    return factorial(n-1) * n

# n = factorial(5)
# print(n)

# fibonacci memoization
mem = dict()
def fibonacci_memoization(n):
    if n in [0, 1]: return n
    if n in mem: return mem[n]
    mem[n] = fibonacci_memoization(n-2) + fibonacci_memoization(n-1)
    return mem[n]

# n = fibonacci_memoization(6, {})
# print(n)

# fibonacci memoization
def fibonacci_memoization(n, mem):
    if n in [0, 1]: return n
    if n in mem: return mem[n]
    mem[n] = fibonacci_memoization(n-2, mem) + fibonacci_memoization(n-1, mem)
    return mem[n]

# n = fibonacci_memoization(6, {})
# print(n)
