S = 'ADBECFCEBAN'
T = 'ABC'

def min_substring(s,t):
    left = 0
    right = 0
    need={}
    window = {}
    valid  = 0
    #确定子串需求
    for i in T:
        if i in need.keys():
            need[i] = need[i] + 1
            continue          
        need[i] = 1  
       
    while right < len(s):
    #右移窗口  
        c = s[right]
        right += 1
        #窗口内的数据更新
        #如果该字符是我们需要的，则更新窗口数据
        if c in t:
            if c in window.keys():
                window[c] = window[c] + 1
            else:          
                window[c] = 1 
            if window[c] == need[c]:
                valid += 1
    #判断左侧是否需要收缩
        while valid == len(need): #说明T中子串已经被覆盖
            #最小覆盖子串的起点终点
            start = left 
            end = right - left
            #d是要移出窗口的字符
            d = s[left]
            #左移窗口
            left += 1
            #如果该字符是子串内的，则对窗口内的数据更新
            if d in t:
                #窗口内数据和需要的相同
                if window[d] == need[d]:
                    valid -= 1
                #窗口内该字符数量大于需要的
                window[d] -= 1
    
    return s[start:start+end]
        
print(min_substring(S,T))

    
