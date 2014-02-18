def selSort(nums):
    # sort nums into ascending order

    n = len(nums)

    # For each position in the list (except the very last)
    for bottom in range(n - 1):
        # find the smallest item in nums[bottom]...nums[n - 1]

        mp = bottom
        for i in range(bottm + 1, n):
            if nums[i] < nums[mp]:
                mp = i

        # swap smallest item to the bottom
        nms[bottom], nums[mp] = nums[mp], nums[bottom]