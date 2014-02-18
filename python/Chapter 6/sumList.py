def sumList(nums):
    # nums is a list of numbers. Returns the sum of the numbers in the list.
    total = 0
    for n in nums:
        total += n
    return total


def main():
    numbers = [1, 2, 3]
    total = sumList(numbers)
    print(total)


main()