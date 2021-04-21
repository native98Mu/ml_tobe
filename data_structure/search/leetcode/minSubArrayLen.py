'''
寻找数字一子序列，使得其相加大于等于目标值 返回子序列长度
滑动窗口方法
'''

def minSubArrayLen(s,nums):
        
        window_start = 0
        min_size = float('inf')
		
		# summation of subarray
        summation = 0
        
        # use sliding window to update min_size of of valid subarray
        for window_end, number in enumerate(nums):
            
            summation += number
            
            while summation >= s:
                
                # keep shrinking window size if summation is valid
                min_size = min( min_size, window_end - window_start + 1)
                
                # update subarray sum
                summation -= nums[window_start]
                
                window_start += 1
                
        
        if min_size == float('inf'):
            
            # no solution
            return 0
        
        else:
            
            return min_size

ls = [1,3,10,4,1,1,13]
print('min size: ',minSubArrayLen(15,ls))
        