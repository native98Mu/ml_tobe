'''
数组共有n+1个元素 均为[1,n]间的整数 寻找其中重复的元素
'''
def findDuplicate(nums):
    arr = [0] * len(nums)
    for i in nums:
        if arr[i]: 
            return i
        else: 
            arr[i] = 1 
ls = [1,2,3,4,5,2]
print('duplicated: ',findDuplicate(ls))