# average4.py
import math


def getNumbers():
    nums = []

    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = int(xStr)
        nums.append(x)
        xStr = input("Enter a number (<Enter> to quit) >> ")
    return nums


def stdDev(nums, xbar):
    sumDevSq = 0.0
    for num in nums:
        dev = xbar - num
        sumDevSq = sumDevSq + dev * dev
    return math.sqrt(sumDevSq / (len(nums) - 1))


def mean(nums):
    sum = 0.0
    for num in nums:
        sum = sum + num
    return sum / len(nums)


def median(nums):
    # sort the numbers into ascending order
    nums.sort()
    size = len(nums)
    midPos = size // 2
    # if the size of data is odd:
    if size % 2 ==0:
    #    median = the middle value
        median = (nums[midPos] + nums[midPos - 1] / 2)
    # else:
    else:
    #    median = the average of the two middle values
        median = nums[midPos]
    # return median
    return median


def main():
    data = getNumbers()
    xbar = mean(data)
    std = stdDev(data, xbar)
    med = median(data)

    print("\nThe mean is", mean(data))
    print("The standard deviation is", std)
    print("The median is", med)


if __name__ in ['__console__', '__main__']:
    main()