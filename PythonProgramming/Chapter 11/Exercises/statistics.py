# statistics.py
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
    # Returns the mean of numbers in nums
    m = 0
    j = 1
    for n in nums:
        m += n
        j += 1
    mean = m / j


def meanStdDev(nums):
    # returns both the mean and standard deviation of nums
    m = mean(nums)
    sd = stdDev(nums, m)

    return m, sd


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
    mean, std = meanStdDev(data)
    med = median(data)

    print("\nThe mean is", mean(data))
    print("The standard deviation is", std)
    print("The median is", med)


if __name__ in ['__console__', '__main__']:
    main()