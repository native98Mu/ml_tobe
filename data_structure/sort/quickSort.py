def swap(arr, i, j):
    arr[j],arr[i] = arr[i],arr[j]

def quick_sort(arr,left,right):
    if left >= right:
        return
    pivot = arr[left] #分界点
    i = left - 1  #左指针
    j = right + 1  #右指针

#如果写成是i = left, j = right, while内去掉i,j的加一操作，while很可能会死循环

    while i < j: #循环迭代
        i += 1
        j -= 1
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        #两指针停下来后，如果还没相遇，交换两数字
        if i < j:
            swap(arr,i,j)
            print(arr)
    quick_sort(arr,left,j)
    quick_sort(arr,j+1,right)
            
ls = [4,2,5,3,6,4,1]
quick_sort(ls,0,len(ls) - 1)


