def squareEach(nums):
    n = []
    for i in nums:
        n.append(i ** 2)

    return n


def main():
    numbers = input("Enter a list of numbers separated by a comma: ")
    numbers = numbers.split(",")
    num = []
    for n in numbers:
        nn = int(n)
        num.append(nn)
    print(squareEach(num))


main()