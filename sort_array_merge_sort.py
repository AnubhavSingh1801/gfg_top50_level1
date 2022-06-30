"""
Time Complexity - O(NlogN)
Space Complexity- O(N)
"""

def merge(arr, l, r, mid):
    left = arr[l:mid+1]
    right = arr[mid+1:r+1]
    
    i, j, k = 0, 0, l
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        elif left[i] > right[j]:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        

def merge_sort(arr, l, r):
    if l<r:
        mid = (l+r)//2
        
        merge_sort(arr, l, mid)
        merge_sort(arr, mid+1, r)
        merge(arr, l, r, mid)
    return arr

def sortArr(arr, n): 
    #code here
    l, r = 0, n-1
    merge_sort(arr, l, r)
    return arr


if __name__ == "__main__":
    arr = [5,4,3,2,1,9,8,7,6]
    n = len(arr)
    print(sortArr(arr,n))