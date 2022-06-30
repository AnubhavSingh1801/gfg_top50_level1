def partition(arr, l, r):
    pivot = arr[l]
    i, j = l-1, r+1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        
        j -= 1
        while arr[j] > pivot:
            j -= 1
        
        if i >= j:
            return j
        
        arr[i], arr[j] = arr[j], arr[i]

def sort(arr, l, r):
    if l<r:
        p = partition(arr, l, r)
        sort(arr, l, p)
        sort(arr, p+1, r)

def quick_sort(arr, n):
    l, r = 0, n-1
    sort(arr, l, r)

if __name__ == "__main__":
    arr = [9,8,7,6,5,3,10,1,27]
    n = len(arr)
    quick_sort(arr, n)
    print(arr)