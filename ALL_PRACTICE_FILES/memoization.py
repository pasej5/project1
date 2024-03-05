#!/usr/bin/env python3

# fibonacci_cache = {}

# def fibonacci(n):
#     # first check if the value of the nth is in the cache
#     if n in fibonacci_cache:
#         return fibonacci_cache[n]
    
#     if n == 1:
#         value = 1
#     elif n == 2:
#         value = 1
#     elif n > 2:
#         value = fibonacci(n - 1) + fibonacci(n - 2)
        
#     fibonacci_cache[n] = value
#     return value
# for n in range(1, 5000):
#     print(n, ":", fibonacci(n))

from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)
# for n in range(1, 500):
#     print(n, ":", fibonacci(n))
fibonacci("one")
