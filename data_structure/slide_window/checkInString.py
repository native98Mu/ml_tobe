S = 'ADBECFBCBADN'
T = 'ABBCD'
def checkInString(s,t):
    need ={}
    window = {}
    left = 0
    right = 0
    valid = 0
    #确定子串需求
    for i in T:
        if i in need.keys():
            need[i] = need[i] + 1
            continue          
        need[i] = 1  
    while right < len(s):
        c = s[right]
        right += 1
        #窗口向右扩大
        #判断该字符是否属于子串
        if c in t:
            if c in window.keys():
                window[c] += 1
            else:
                window[c] = 1
            if window[c] == need[c]:
                valid += 1
        #是否需要收缩
        while right -left >= len(t):
            if valid == len(need):
                return True
            d = s[left]
            left += 1
            if d in t:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
    return False
# def checkInString(s,t):
#     need ={}
#     window = {}
#     left = 0
#     right = 0
#     valid = 0
#     #确定子串需求
#     for i in T:
#         if i in need.keys():
#             need[i] = need[i] + 1
#             continue          
#         need[i] = 1  
#     while right < len(s):
#         c = s[right]
#         right += 1
#         #判断该字符是否属于子串
#         if c in t:
#             if c in window.keys():
#                 window[c] += 1
#             else:
#                 window[c] = 1
#             if window[c] == need[c]:
#                 valid += 1
#         else:
#             left = right
#             window = {}
#             valid = 0 
#         if valid == len(need):
#             return s[left:right]
    # return False
print(checkInString(S,T))