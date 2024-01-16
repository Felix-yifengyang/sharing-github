import sys
def BubbleSort (arr) :
    n = len(arr)
    for i in range (n-1) :
        swapped = False
        for j in range (n-i-1) :
            if arr[j] > arr[j+1] :
                swapped = True
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if not swapped :         #一旦没有交换，证明排序完成
            return 
arr = [99,88,55,77,1,66]
BubbleSort(arr)
print(arr)