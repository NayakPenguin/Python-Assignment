def fibonacci_generator(n):
    a, b = 0, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1

n = int(input("Enter the number of Fibonacci numbers required : "))
fibonacci = fibonacci_generator(n)

print("First seven Fibonacci numbers:")
for _ in range(n):
    print(next(fibonacci))
