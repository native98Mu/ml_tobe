def lengthOfLongestSubstring(s):
    left = 0
    right = 0
    window = {}
    res = 0
    while right < len(s):
        c = s[right]
        right += 1
        #判断是否需要进行收缩
        if c in window.keys():
            window[c] += 1
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
        window[c] = 1
        res = max(res, right-left)
    return res

            
s = 'afdadae'
print(lengthOfLongestSubstring(s))
