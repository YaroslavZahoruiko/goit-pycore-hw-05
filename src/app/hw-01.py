def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n < 2:
            return n
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci


if __name__ == "__main__":
    fib = caching_fibonacci()
    print(fib(10))
    print(fib(15))
