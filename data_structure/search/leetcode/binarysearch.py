def binarySearch(nums,target):
    right = len(nums) - 1
    left = 0
    while (left <= right):
        mid = left + int((right - left)/2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid-1
    return left

ls = [1,3,5,6]
print('Position: ',binarySearch(ls,9))