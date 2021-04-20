def left_bound(nums,target):
    left = 0
    right = len(nums)
    if len(nums) == 0:
        return
    while left < right:
        mid = left + int((right - left) / 2)
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid
    return left
def right_bound(nums,target):
    left = 0
    right = len(nums)
    if len(nums) == 0:
        return 
    while left < right:
        mid = left + int((right-left)/2)
        if nums[mid] == target:
            left = mid+1
        elif nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid
    return left-1
ls = [1,2,3,3,3,4,5]
print(left_bound(ls,3))
print(right_bound(ls,3))