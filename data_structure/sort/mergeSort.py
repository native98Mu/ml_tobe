tmp = []
def merge_sort(arr,left,right):
    if left >= right:
        return
    #分组
    mid = int((left + right) / 2)
    merge_sort(arr,left,mid)
    merge_sort(arr,mid+1,right)

    #合并两组
    k = 0
    i = left
    j = mid + 1
    while i <= mid & j <= right:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            k += 1
            i += 1
        else:
            tmp[k] = arr[j]
            k += 1 
            j += 1
    while i <= mid:
        k += 1
        i += 1
        tmp[k] = arr[i]
    while j <= right:
        k += 1 
        j += 1
        tmp[k] = arr[j]    
    arr = tmp[:]
    print(arr)

ls= [1,2,7,3,2,8,5]
merge_sort(ls,0,len(ls)-1)