def search(nums,target):
    max = 0
    index = 0
    for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i]
            index = i
    #前半部分
    left = 0 
    right = index
    while left <= right:
        mid = left + int((right-left)/2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    left = index + 1
    right = len(nums) - 1
    while left <= right:
        mid = left + int((right-left)/2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1

ls = [4,5,6,7,0,1,2]
num = 0
search(ls,num)