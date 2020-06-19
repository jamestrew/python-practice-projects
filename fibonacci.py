def fibonacci_v1(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    return fibonacci_v1(n-1) + fibonacci_v1(n-2)


def list_fibonacci(n):
    for i in range(1, n+1):
        print(fibonacci_v1(i))

list_fibonacci(10)
