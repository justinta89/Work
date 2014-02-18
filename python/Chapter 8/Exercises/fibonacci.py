# fibonacci.py
# Calculates the nth number in fibonacci sequence.


def fibonacci(n):
    if n > 0:
        if n == 1:
            fn = 1
        elif n == 0:
            fn = 0
        else:
            fn = (n - 1) + (n - 2)
    if n < 0:
        if n == -1:
            fn = 1
        else:
            fn = ((-1) ** (n + 1)) * n

    return fn


def main():
    num = int(input("Enter a number >> "))
    print(fibonacci(num))


if __name__ in ['__console__', '__main__']:
    main()